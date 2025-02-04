import os
from typing import Dict, List, Optional

import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np
import polars as pl
import scienceplots  # noqa: F401
import seaborn as sns
from scipy import stats

plt.style.use("science")


class VectorizedRiskSetMatcher:
    def __init__(self, config: Dict):
        self._validate_config(config)
        self.n_matches = config["n_matches"]
        self.exact_match_cols = config.get("exact_match_cols", ["fm_living"])
        self.child_date_tolerance = config.get("child_date_tolerance", 30)  # days
        self.parent_date_tolerance = config.get("parent_date_tolerance", 365.25)  # days
        self.allow_replacement = config.get("allow_replacement", False)
        self.match_vars = [
            "mother_age_at_birth_norm",
            "father_age_at_birth_norm",
        ]

        # Define variables to be balanced
        self.balance_vars = [
            "mother_age_at_birth_norm",
            "father_age_at_birth_norm",
        ]
        self.match_var_weights = config.get(
            "match_var_weights", {var: 1.0 for var in self.match_vars}
        )
        self.balance_tolerance = config.get("balance_tolerance", 0.1)
        self.variance_tolerance = config.get("variance_tolerance", 0.2)
        self.solver_options = config.get(
            "solver_options",
            {
                "limits/time": 300,
                "display/verblevel": 2,
                "numerics/feastol": 1e-6,
                "presolving/maxrounds": 10,
                "separating/maxrounds": 10,
                "limits/gap": 0.01,
                "lp/threads": 4,
            },
        )

    def _validate_config(self, config: Dict) -> None:
        required_params = ["n_matches"]
        if missing := [param for param in required_params if param not in config]:
            raise ValueError(f"Missing required parameters: {missing}")

    def prepare_data(self, data_path: str) -> pl.DataFrame:
        df = pl.scan_csv(data_path)

        # First convert dates
        df = df.with_columns(
            [
                pl.col("pnr").cast(pl.Utf8),
                *[
                    pl.col(col).str.strptime(pl.Date, format="%Y-%m-%d")
                    for col in [
                        "child_birthdate",
                        "mother_birthdate",
                        "father_birthdate",
                        "diagnosis_date",
                    ]
                ],
            ]
        )

        # Calculate all required fields in one pass
        df = df.with_columns(
            [
                # Parent ages at birth
                (
                    (
                        pl.col("child_birthdate") - pl.col("mother_birthdate")
                    ).dt.total_days()
                    / 365.25
                ).alias("mother_age_at_birth"),
                (
                    (
                        pl.col("child_birthdate") - pl.col("father_birthdate")
                    ).dt.total_days()
                    / 365.25
                ).alias("father_age_at_birth"),
                # Treatment indicators
                pl.col("diagnosis_date").is_not_null().alias("treatment_status"),
                pl.col("diagnosis_date").alias("treatment_time"),
                # Epoch days for matching
                pl.col("child_birthdate").dt.epoch("d").alias("child_birth_days"),
                pl.col("mother_birthdate").dt.epoch("d").alias("mother_birth_days"),
                pl.col("father_birthdate").dt.epoch("d").alias("father_birth_days"),
            ]
        )

        # Normalize age variables in one operation
        df = df.with_columns(
            [
                ((pl.col(col) - pl.col(col).mean()) / pl.col(col).std()).alias(
                    f"{col}_norm"
                )
                for col in ["mother_age_at_birth", "father_age_at_birth"]
            ]
        )

        return df.collect()

    def find_matches(self, df: pl.DataFrame) -> pl.DataFrame:
        """Find matches using vectorized operations"""
        # Split data into treated and control
        treated_df = df.filter(pl.col("diagnosis_date").is_not_null())
        control_df = df.filter(pl.col("diagnosis_date").is_null())

        # Create treated and control matrices
        treated_covs = treated_df.select(self.match_vars).to_numpy()
        control_covs = control_df.select(self.match_vars).to_numpy()

        # Calculate distance matrix for all pairs
        distances = self._calculate_mahalanobis_distance_batch(
            treated_covs, control_covs
        )

        # Create eligibility matrix
        eligibility = self._create_eligibility_matrix(treated_df, control_df)

        # Mask distances with eligibility
        distances[~eligibility] = np.inf

        # Solve optimization problem
        matches = self._solve_optimization_batch(distances, treated_df, control_df)

        return matches if not matches.is_empty() else self._empty_matches_df()

    def _calculate_mahalanobis_distance_batch(
        self, treated_covs: np.ndarray, control_covs: np.ndarray
    ) -> np.ndarray:
        """Calculate Mahalanobis distances for all pairs at once"""
        epsilon = 1e-6
        all_covs = np.vstack([treated_covs, control_covs])
        cov = np.cov(all_covs.T) + epsilon * np.eye(all_covs.shape[1])
        inv_cov = np.linalg.pinv(cov)

        # Use broadcasting for distance calculation
        diff = treated_covs[:, np.newaxis, :] - control_covs[np.newaxis, :, :]
        return np.sqrt(np.einsum("ijk,kl,ijl->ij", diff, inv_cov, diff))

    def _create_eligibility_matrix(
        self, treated_df: pl.DataFrame, control_df: pl.DataFrame
    ) -> np.ndarray:
        """Create eligibility matrix for all treated-control pairs"""
        n_treated = len(treated_df)
        n_controls = len(control_df)

        # Broadcast date comparisons
        treated_dates = {
            "child": treated_df.get_column("child_birth_days").to_numpy()[
                :, np.newaxis
            ],
            "mother": treated_df.get_column("mother_birth_days").to_numpy()[
                :, np.newaxis
            ],
            "father": treated_df.get_column("father_birth_days").to_numpy()[
                :, np.newaxis
            ],
            "treatment": treated_df.get_column("treatment_time").to_numpy()[
                :, np.newaxis
            ],
        }

        control_dates = {
            "child": control_df.get_column("child_birth_days").to_numpy()[
                np.newaxis, :
            ],
            "mother": control_df.get_column("mother_birth_days").to_numpy()[
                np.newaxis, :
            ],
            "father": control_df.get_column("father_birth_days").to_numpy()[
                np.newaxis, :
            ],
            "treatment": control_df.get_column("treatment_time").to_numpy()[
                np.newaxis, :
            ],
        }

        # Date eligibility
        date_eligible = (
            (
                np.abs(treated_dates["child"] - control_dates["child"])
                <= self.child_date_tolerance
            )
            & (
                np.abs(treated_dates["mother"] - control_dates["mother"])
                <= self.parent_date_tolerance
            )
            & (
                np.abs(treated_dates["father"] - control_dates["father"])
                <= self.parent_date_tolerance
            )
        )

        # Treatment timing eligibility
        time_eligible = (
            control_dates["treatment"] > treated_dates["treatment"]
        ) | np.isnan(control_dates["treatment"])

        # Exact matching criteria
        exact_eligible = np.ones((n_treated, n_controls), dtype=bool)
        for col in self.exact_match_cols:
            treated_vals = treated_df.get_column(col).to_numpy()[:, np.newaxis]
            control_vals = control_df.get_column(col).to_numpy()[np.newaxis, :]
            exact_eligible &= treated_vals == control_vals

        return date_eligible & time_eligible & exact_eligible

    def _solve_optimization_batch(
        self, distances: np.ndarray, treated_df: pl.DataFrame, control_df: pl.DataFrame
    ) -> pl.DataFrame:
        """Solve optimization problem for all matches at once"""
        n_treated = len(treated_df)
        n_controls = len(control_df)

        # Create assignment matrix
        X = cp.Variable((n_treated, n_controls), boolean=True)

        # Define objective and constraints
        objective = cp.Minimize(cp.sum(cp.multiply(distances, X)))

        constraints = [
            cp.sum(X, axis=1) <= self.n_matches,  # Max matches per treated
            cp.sum(X, axis=0) <= 1,  # Each control used at most once
        ]

        # Add balance constraints
        for var in self.balance_vars:
            treated_vals = treated_df.get_column(var).to_numpy()
            control_vals = control_df.get_column(var).to_numpy()
            balance_diff = cp.sum(
                cp.multiply(X, (treated_vals[:, None] - control_vals[None, :]))
            )
            constraints.append(cp.abs(balance_diff) <= self.balance_tolerance)

        prob = cp.Problem(objective, constraints)

        try:
            prob.solve(solver=cp.SCIP, verbose=False)

            if (
                prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]
                and X.value is not None
            ):
                return self._extract_matches_from_solution(
                    np.asarray(X.value), treated_df, control_df, distances
                )
            return self._empty_matches_df()
        except Exception as e:
            print(f"Optimization failed: {str(e)}")
            return self._empty_matches_df()

    def _extract_matches_from_solution(
        self,
        solution: np.ndarray,
        treated_df: pl.DataFrame,
        control_df: pl.DataFrame,
        distances: np.ndarray,
    ) -> pl.DataFrame:
        """Extract matches from optimization solution in vectorized form"""
        match_indices = np.where(solution > 0.5)

        matches_data = {
            "treated_id": treated_df.get_column("pnr").to_numpy()[match_indices[0]],
            "control_id": control_df.get_column("pnr").to_numpy()[match_indices[1]],
            "treatment_time": treated_df.get_column("treatment_time").to_numpy()[
                match_indices[0]
            ],
            "distance": distances[match_indices],
            "birth_date_diff": np.abs(
                treated_df.get_column("child_birth_days").to_numpy()[match_indices[0]]
                - control_df.get_column("child_birth_days").to_numpy()[match_indices[1]]
            ),
            "mother_birth_date_diff": np.abs(
                treated_df.get_column("mother_birth_days").to_numpy()[match_indices[0]]
                - control_df.get_column("mother_birth_days").to_numpy()[
                    match_indices[1]
                ]
            ),
            "father_birth_date_diff": np.abs(
                treated_df.get_column("father_birth_days").to_numpy()[match_indices[0]]
                - control_df.get_column("father_birth_days").to_numpy()[
                    match_indices[1]
                ]
            ),
        }

        return pl.DataFrame(matches_data)

    def evaluate_matches(
        self, matches: pl.DataFrame, original_df: pl.DataFrame
    ) -> Dict:
        """Evaluate matching results with combined metrics"""
        evaluation = (
            matches.join(
                original_df.with_columns(pl.col("pnr").cast(pl.Utf8)),
                left_on="treated_id",
                right_on="pnr",
            )
            .join(
                original_df.with_columns(pl.col("pnr").cast(pl.Utf8)),
                left_on="control_id",
                right_on="pnr",
                suffix="_control",
            )
            .group_by("treated_id")
            .agg(
                [
                    pl.col("distance").mean().alias("avg_distance"),
                    pl.col("distance").std().alias("std_distance"),
                    pl.col("control_id").count().alias("n_matches"),
                    *[
                        pl.col(var).mean().alias(f"{var}_treated_mean")
                        for var in self.match_vars
                    ],
                    *[
                        pl.col(f"{var}_control").mean().alias(f"{var}_control_mean")
                        for var in self.match_vars
                    ],
                ]
            )
        )

        return {
            "balance_metrics": evaluation,
            "summary": self._calculate_summary_stats(matches),
        }

    def _calculate_summary_stats(self, matches: pl.DataFrame) -> Dict:
        """Calculate summary statistics"""
        if matches.is_empty():
            return {
                "total_treated": 0,
                "total_matches": 0,
                "avg_matches_per_treated": 0,
                "median_distance": 0,
                "mean_distance": 0,
            }

        return {
            "total_treated": len(matches["treated_id"].unique()),
            "total_matches": len(matches),
            "avg_matches_per_treated": len(matches)
            / len(matches["treated_id"].unique()),
            "median_distance": matches["distance"].median(),
            "mean_distance": matches["distance"].mean(),
        }

    def _empty_matches_df(self) -> pl.DataFrame:
        """Create empty matches DataFrame with correct schema"""
        return pl.DataFrame(
            schema={
                "treated_id": pl.Utf8,
                "control_id": pl.Utf8,
                "treatment_time": pl.Date,
                "distance": pl.Float64,
                "birth_date_diff": pl.Int64,
                "mother_birth_date_diff": pl.Int64,
                "father_birth_date_diff": pl.Int64,
            }
        )

    def analyze_matches(
        self,
        matches: pl.DataFrame,
        original_df: pl.DataFrame,
        output_dir: str = "output",
    ):
        """Analyze and visualize matching results"""
        os.makedirs(output_dir, exist_ok=True)

        if matches.is_empty():
            print("Warning: No matches found. Skipping analysis.")
            return {
                "match_stats": {
                    "n_treated": 0,
                    "n_controls": 0,
                    "avg_matches_per_treated": 0,
                    "max_distance": 0,
                    "mean_distance": 0,
                    "median_distance": 0,
                },
                "balance_stats": pl.DataFrame(
                    {
                        "variable": self.match_vars,
                        "treated_mean": [0] * len(self.match_vars),
                        "control_mean": [0] * len(self.match_vars),
                        "std_diff": [0] * len(self.match_vars),
                    }
                ),
            }

        # Create analyzer instance
        analyzer = MatchingAnalyzer(original_df, matches)

        # Define variables for balance checking
        balance_vars = [
            "mother_age_at_birth",
            "father_age_at_birth",
            "child_birth_days",
            "mother_birth_days",
            "father_birth_days",
            "mother_age_at_birth_norm",
            "father_age_at_birth_norm",
        ]

        # Compute statistics
        match_stats = analyzer.compute_match_statistics()
        balance_stats = analyzer.compute_balance_statistics(balance_vars)

        # Generate plots
        analyzer.plot_distance_distribution(save_path=f"{output_dir}/matching")
        analyzer.plot_date_differences(save_path=f"{output_dir}/matching")
        analyzer.plot_balance_diagnostics(
            balance_stats, save_path=f"{output_dir}/matching"
        )
        analyzer.plot_qq_plots(balance_vars, save_path=f"{output_dir}/matching")
        analyzer.plot_love_plot(balance_stats, save_path=f"{output_dir}/matching")

        # Generate summary report
        analyzer.generate_summary_report(
            balance_vars, f"{output_dir}/matching_report.txt"
        )

        return {"match_stats": match_stats, "balance_stats": balance_stats}


class MatchingAnalyzer:
    def __init__(self, original_data: pl.DataFrame, matches: pl.DataFrame):
        self.original_data = original_data
        self.matches = matches
        self.treated_ids = matches.get_column("treated_id").unique()
        self.control_ids = matches.get_column("control_id").unique()

        # Set default plot style
        plt.style.use(["science", "ieee"])

    def compute_match_statistics(self) -> Dict:
        """Compute basic matching statistics"""
        if self.matches.is_empty():
            return {
                "n_treated": 0,
                "n_controls": 0,
                "avg_matches_per_treated": 0,
                "max_distance": 0,
                "mean_distance": 0,
                "median_distance": 0,
            }

        def safe_float(value: Optional[float]) -> float:
            """Safely convert value to float, returning 0.0 if None"""
            return float(value) if value is not None else 0.0

        def safe_stat(series: pl.Series, func: str) -> float:
            """Safely compute statistic, handling None values"""
            result = getattr(series, func)()
            return safe_float(result)

        n_treated = len(self.treated_ids)
        if n_treated == 0:
            return {
                "n_treated": 0,
                "n_controls": len(self.control_ids),
                "avg_matches_per_treated": 0,
                "max_distance": 0,
                "mean_distance": 0,
                "median_distance": 0,
            }

        stats = {
            "n_treated": n_treated,
            "n_controls": len(self.control_ids),
            "avg_matches_per_treated": len(self.matches) / n_treated,
        }

        # Distance statistics
        distance_col = self.matches.get_column("distance")
        stats.update(
            {
                "max_distance": safe_stat(distance_col, "max"),
                "mean_distance": safe_stat(distance_col, "mean"),
                "median_distance": safe_stat(distance_col, "median"),
            }
        )

        # Date difference statistics (in days)
        for diff_col in [
            "birth_date_diff",
            "mother_birth_date_diff",
            "father_birth_date_diff",
        ]:
            col = self.matches.get_column(diff_col)
            stats.update(
                {
                    f"{diff_col}_mean": safe_stat(col, "mean"),
                    f"{diff_col}_median": safe_stat(col, "median"),
                    f"{diff_col}_max": safe_stat(col, "max"),
                }
            )

        return stats

    def plot_distance_distribution(self, save_path: Optional[str] = None):
        """Plot the distribution of matching distances"""
        with plt.style.context(["science", "ieee"]):
            fig, ax = plt.subplots(figsize=(6, 4))

            data = self.matches.to_pandas()
            sns.histplot(data=data, x="distance", bins=30, ax=ax)

            ax.set_xlabel("Matching Distance")
            ax.set_ylabel("Count")
            ax.set_title("Distribution of Matching Distances")

            if save_path:
                plt.savefig(f"{save_path}_distances.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    def plot_date_differences(self, save_path: Optional[str] = None):
        """Plot the distribution of date differences"""
        with plt.style.context(["science", "ieee", "grid"]):
            fig, axes = plt.subplots(1, 3, figsize=(12, 4))

            date_cols = [
                "birth_date_diff",
                "mother_birth_date_diff",
                "father_birth_date_diff",
            ]
            titles = ["Child Birth Date", "Mother Birth Date", "Father Birth Date"]
            ylabels = ["Days Difference", "Days Difference", "Days Difference"]

            data = self.matches.to_pandas()

            for ax, col, title, ylabel in zip(axes, date_cols, titles, ylabels):
                sns.boxplot(y=data[col], ax=ax)
                ax.set_title(title)
                ax.set_ylabel(ylabel)

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_date_diffs.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    def plot_balance_diagnostics(
        self, balance_stats: pl.DataFrame, save_path: Optional[str] = None
    ):
        """Create balance diagnostic plots"""
        with plt.style.context(["science", "ieee", "grid"]):
            fig, ax = plt.subplots(figsize=(8, 6))

            data = balance_stats.to_pandas()

            # Plot standardized differences
            sns.barplot(data=data, x="variable", y="std_diff", ax=ax)

            # Add reference lines
            ax.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
            ax.axhline(y=0.1, color="r", linestyle="--", linewidth=0.5)
            ax.axhline(y=-0.1, color="r", linestyle="--", linewidth=0.5)

            ax.set_xlabel("Variables")
            ax.set_ylabel("Standardized Difference")
            ax.set_title("Covariate Balance")

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45, ha="right")

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_balance.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    def compute_balance_statistics(self, variables: List[str]) -> pl.DataFrame:
        """Compute standardized differences for specified variables"""
        treated_data = self.original_data.filter(pl.col("pnr").is_in(self.treated_ids))
        control_data = self.original_data.filter(pl.col("pnr").is_in(self.control_ids))

        balance_stats = []
        for var in variables:
            treated_vals = treated_data.get_column(var).to_numpy()
            control_vals = control_data.get_column(var).to_numpy()

            # Vectorized statistics computation
            treated_mean = np.mean(treated_vals)
            control_mean = np.mean(control_vals)
            pooled_std = np.sqrt((np.var(treated_vals) + np.var(control_vals)) / 2)

            std_diff = (
                (treated_mean - control_mean) / pooled_std if pooled_std != 0 else 0
            )

            balance_stats.append(
                {
                    "variable": var,
                    "treated_mean": float(treated_mean),
                    "control_mean": float(control_mean),
                    "std_diff": float(std_diff),
                }
            )

        return pl.DataFrame(balance_stats)

    def generate_summary_report(self, variables: List[str], output_path: str):
        """Generate a comprehensive matching summary report"""
        # Compute all statistics
        match_stats = self.compute_match_statistics()
        balance_stats = self.compute_balance_statistics(variables)

        # Create report
        with open(output_path, "w") as f:
            f.write("Matching Analysis Summary Report\n")
            f.write("==============================\n\n")

            f.write("1. Basic Statistics\n")
            f.write("-----------------\n")
            for key, value in match_stats.items():
                f.write(f"{key}: {value:.2f}\n")

            f.write("\n2. Balance Statistics\n")
            f.write("-------------------\n")
            f.write(balance_stats.to_pandas().to_string())

        # Generate all plots
        self.plot_distance_distribution(output_path)
        self.plot_date_differences(output_path)
        self.plot_balance_diagnostics(balance_stats, output_path)

    def plot_qq_plots(self, variables: List[str], save_path: Optional[str] = None):
        """Create Q-Q plots for continuous variables"""
        with plt.style.context(["science", "ieee", "grid"]):
            n_vars = len(variables)
            n_cols = 3
            n_rows = (n_vars + n_cols - 1) // n_cols

            fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4 * n_rows))
            axes = axes.ravel()

            treated_data = self.original_data.filter(
                pl.col("pnr").is_in(self.treated_ids)
            )
            control_data = self.original_data.filter(
                pl.col("pnr").is_in(self.control_ids)
            )

            for idx, var in enumerate(variables):
                treated_vals = treated_data.get_column(var).to_numpy()
                control_vals = control_data.get_column(var).to_numpy()

                # Create Q-Q plot
                stats.probplot(treated_vals, dist="norm", plot=axes[idx])
                stats.probplot(control_vals, dist="norm", plot=axes[idx])

                axes[idx].set_title(f"Q-Q Plot: {var}")

            # Remove empty subplots
            for idx in range(len(variables), len(axes)):
                fig.delaxes(axes[idx])

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_qq_plots.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    def plot_love_plot(
        self, balance_stats: pl.DataFrame, save_path: Optional[str] = None
    ):
        """Create a Love plot showing standardized differences before and after matching"""
        with plt.style.context(["science", "ieee", "grid"]):
            fig, ax = plt.subplots(figsize=(8, len(balance_stats) * 0.3))

            data = balance_stats.to_pandas()
            data = data.sort_values("std_diff", key=abs)

            y_pos = np.arange(len(data))
            ax.barh(y_pos, data["std_diff"])

            ax.axvline(x=0, color="k", linestyle="-", linewidth=0.5)
            ax.axvline(x=0.1, color="r", linestyle="--", linewidth=0.5)
            ax.axvline(x=-0.1, color="r", linestyle="--", linewidth=0.5)

            ax.set_yticks(y_pos)
            ax.set_yticklabels(data["variable"])
            ax.set_xlabel("Standardized Difference")
            ax.set_title("Love Plot: Covariate Balance")

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_love_plot.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()


def main():
    config = {
        "n_matches": 10,
        "exact_match_cols": ["fm_living"],
        "child_date_tolerance": 30,  # 30 days for child
        "parent_date_tolerance": 365.25,  # 1 year for parents
        "allow_replacement": False,
        "balance_tolerance": 0.2,  # 10% tolerance for balance constraints
        "solver_options": {
            "limits/time": 300,
            "display/verblevel": 2,
            "numerics/feastol": 1e-6,
            "presolving/maxrounds": 10,
            "separating/maxrounds": 10,
            "limits/gap": 0.05,  # 5% gap tolerance
            "lp/threads": 4,  # number of threads to use
        },
    }

    print("Starting matching process...")
    matcher = VectorizedRiskSetMatcher(config)

    print("Loading data...")
    df = matcher.prepare_data("test_data.csv")

    print("Finding matches...")
    matches = matcher.find_matches(df)

    print("\nGenerating analysis and plots...")
    analysis_results = matcher.analyze_matches(matches, df, output_dir="output")

    print("\nMatching Results:")
    print(f"Total matches found: {len(matches)}")
    print(f"Unique treated subjects: {len(matches['treated_id'].unique())}")
    print(f"Unique control subjects: {len(matches['control_id'].unique())}")

    print("\nAnalysis Results:")
    print("Match Statistics:")
    for key, value in analysis_results["match_stats"].items():
        print(f"{key}: {value:.2f}")

    print("\nBalance Statistics:")
    print(analysis_results["balance_stats"])


if __name__ == "__main__":
    main()
