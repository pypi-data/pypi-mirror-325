import os
from typing import Dict, List, Optional

import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import polars as pl
import scienceplots  # noqa: F401
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.container import Container
from scipy import stats as scipy_stats

plt.style.use("science")


class VectorizedRiskSetMatcher:
    def __init__(self, config: Dict):
        self._validate_config(config)
        self.n_matches = config["n_matches"]
        self.exact_match_cols = [
            col for col in config.get("exact_match_cols", []) if col != "fm_living"
        ]
        self.child_date_tolerance = config.get("child_date_tolerance", 30)  # days
        self.parent_date_tolerance = config.get("parent_date_tolerance", 365.25)  # days
        self.allow_replacement = config.get("allow_replacement", False)
        self.match_vars = [
            "mother_age_at_birth_norm",
            "father_age_at_birth_norm",
            # "child_birth_days",
            # "mother_birth_days",
            # "father_birth_days",
        ]

        # Define variables to be balanced
        self.balance_check_vars = {
            "static": [
                "mother_age_at_birth",
                "father_age_at_birth",
            ],  # truly static variables
            "time_varying": [
                "mother_education",
                "father_education",
                "mother_annual_income",
                "father_annual_income",
                "mother_employment",
                "father_employment",
            ],
        }

        self.match_var_weights = config.get(
            "match_var_weights", {var: 1.0 for var in self.match_vars}
        )
        self.balance_tolerance = config.get("balance_tolerance", 0.1)
        self.variance_tolerance = config.get("variance_tolerance", 0.2)
        self.solver_options = config.get(
            "solver_options",
            {
                "limits/time": 300,  # time limit in seconds
                "display/verblevel": 2,  # verbosity level (0-5)
                "numerics/feastol": 1e-6,  # feasibility tolerance
                "presolving/maxrounds": 10,  # maximum number of presolving rounds
                "separating/maxrounds": 10,  # maximum number of separation rounds
                "limits/gap": 0.01,  # relative gap tolerance
            },
        )

        # Add paths for time-varying covariate files
        self.income_history_path = config.get(
            "income_history_path", "income_history.parquet"
        )
        self.employment_history_path = config.get(
            "employment_history_path", "employment_history.parquet"
        )

        # Add path for education history file
        self.education_history_path = config.get(
            "education_history_path", "data/education_history.parquet"
        )

        # Add path for fm_living history file
        self.fm_living_history_path = config.get(
            "fm_living_history_path", "fm_living_history.parquet"
        )

        # Load fm_living history data and ensure pnr is string type
        self.fm_living_history = pl.scan_parquet(
            self.fm_living_history_path
        ).with_columns(pl.col("pnr").cast(pl.Utf8))

        # Load education history data
        self.education_history = pl.scan_parquet(
            self.education_history_path
        ).with_columns(pl.col("pnr").cast(pl.Utf8))

        # Load time-varying covariate data with consistent pnr type
        self.income_history = pl.scan_parquet(self.income_history_path).with_columns(
            pl.col("pnr").cast(pl.Utf8)
        )
        self.employment_history = pl.scan_parquet(
            self.employment_history_path
        ).with_columns(pl.col("pnr").cast(pl.Utf8))

    def _validate_config(self, config: Dict) -> None:
        required_params = ["n_matches"]
        if missing := [param for param in required_params if param not in config]:
            raise ValueError(f"Missing required parameters: {missing}")

    def _get_education_level(
        self,
        df: pl.DataFrame,
        reference_date_col: str,
        id_col: str = "pnr",  # Add id_col parameter with default value
    ) -> pl.DataFrame:
        """
        Get education level for parents at the reference date using LazyFrame

        Args:
            df: DataFrame containing the main data
            reference_date_col: Column name for reference date
            id_col: Column name containing the person identifier (default: "pnr")
        """
        # Convert reference dates from main dataframe to a column we can use for joining
        df_with_date = df.with_columns(
            [
                pl.col(reference_date_col).alias("reference_date"),
                pl.col(id_col).alias("pnr"),  # Create pnr column from id_col
            ]
        ).lazy()

        # Get latest education level before reference date for each parent
        education_levels = (
            self.education_history
            # Join with main data to get reference dates
            .join(df_with_date.select(["pnr", "reference_date"]), on="pnr", how="inner")
            # Filter for education records before reference date
            .filter(
                pl.col("date").cast(pl.Date) <= pl.col("reference_date").cast(pl.Date)
            )
            .group_by(["pnr", "type"])
            .agg([pl.col("education_level").last().alias("education_level")])
            # Group by pnr to get mother and father education in same row
            .group_by("pnr")
            .agg(
                [
                    pl.col("education_level")
                    .filter(pl.col("type") == "mother")
                    .max()
                    .alias("mother_education"),
                    pl.col("education_level")
                    .filter(pl.col("type") == "father")
                    .max()
                    .alias("father_education"),
                ]
            )
        )

        # Join with main data and handle missing values
        return df.join(
            education_levels.collect(),  # Convert to eager mode for joining
            left_on=id_col,  # Use id_col for joining
            right_on="pnr",
            how="left",
        ).with_columns(
            [
                # Fill missing values with 9 (Unknown/Missing)
                pl.col("mother_education").fill_null(9),
                pl.col("father_education").fill_null(9),
            ]
        )

    def _get_fm_living_status(
        self, df: pl.DataFrame, reference_date_col: str
    ) -> pl.DataFrame:
        """
        Get family living arrangement based on reference date
        """
        # Calculate relative year as integer
        df_with_year = df.with_columns(
            [
                self._get_relative_year(
                    pl.col(reference_date_col), pl.col("child_birthdate")
                ).alias("relative_year")
            ]
        )

        # Join with fm_living history
        joined_df = df_with_year.join(
            self.fm_living_history.collect(), left_on="pnr", right_on="pnr"
        )

        # Create a when-then expression to select the appropriate column
        fm_living_expr = (
            pl.when(pl.col("relative_year") == 0)
            .then(pl.col("t0"))
            .when(pl.col("relative_year") == 1)
            .then(pl.col("t1"))
            .when(pl.col("relative_year") == 2)
            .then(pl.col("t2"))
            .when(pl.col("relative_year") == 3)
            .then(pl.col("t3"))
            .when(pl.col("relative_year") == 4)
            .then(pl.col("t4"))
            .when(pl.col("relative_year") == 5)
            .then(pl.col("t5"))
            .when(pl.col("relative_year") == 6)
            .then(pl.col("t6"))
            .otherwise(pl.col("t0"))  # Default to t_0 if outside range
            .alias("fm_living")
        )

        return joined_df.with_columns([fm_living_expr])

    def _get_relative_year(
        self, reference_date: pl.Expr, birth_date: pl.Expr
    ) -> pl.Expr:
        """
        Calculate the relative year (0-6) based on reference date
        """
        return (reference_date.dt.year() - birth_date.dt.year()).clip(
            0, 6
        )  # Ensure we don't go beyond 6

    def _get_time_varying_covariates(
        self, df: pl.DataFrame, reference_date_col: str, id_col: str
    ) -> pl.DataFrame:
        """
        Get time-varying covariates based on reference date for wide-format data

        Args:
            df: DataFrame containing the data
            reference_date_col: Column name for reference date
            id_col: Column name containing the pnr (e.g., 'treated_id' or 'control_id')
        """
        # Calculate relative year
        df_with_year = df.with_columns(
            [
                self._get_relative_year(
                    pl.col(reference_date_col), pl.col("child_birthdate")
                ).alias("relative_year")
            ]
        )

        # Prepare income data
        mother_income = (
            self.income_history.filter(pl.col("type") == "mother")
            .drop("type")
            .collect()
        )

        father_income = (
            self.income_history.filter(pl.col("type") == "father")
            .drop("type")
            .collect()
        )

        # Prepare employment data
        mother_employment = (
            self.employment_history.filter(pl.col("type") == "mother")
            .drop("type")
            .collect()
        )

        father_employment = (
            self.employment_history.filter(pl.col("type") == "father")
            .drop("type")
            .collect()
        )

        # Join with the data
        joined_df = df_with_year

        # Join mother's income data
        if not mother_income.is_empty():
            joined_df = joined_df.join(
                mother_income,
                left_on=id_col,
                right_on="pnr",
                how="left",
            )

        # Join father's income data
        if not father_income.is_empty():
            joined_df = joined_df.join(
                father_income,
                left_on=id_col,
                right_on="pnr",
                how="left",
                suffix="_father",
            )

        # Join mother's employment data
        if not mother_employment.is_empty():
            joined_df = joined_df.join(
                mother_employment,
                left_on=id_col,
                right_on="pnr",
                how="left",
                suffix="_mother_emp",
            )

        # Join father's employment data
        if not father_employment.is_empty():
            joined_df = joined_df.join(
                father_employment,
                left_on=id_col,
                right_on="pnr",
                how="left",
                suffix="_father_emp",
            )

        # Create expressions for selecting time-varying values
        mother_income_expr = (
            pl.when(pl.col("relative_year") == 0)
            .then(pl.col("t0"))
            .when(pl.col("relative_year") == 1)
            .then(pl.col("t1"))
            .when(pl.col("relative_year") == 2)
            .then(pl.col("t2"))
            .when(pl.col("relative_year") == 3)
            .then(pl.col("t3"))
            .when(pl.col("relative_year") == 4)
            .then(pl.col("t4"))
            .when(pl.col("relative_year") == 5)
            .then(pl.col("t5"))
            .when(pl.col("relative_year") == 6)
            .then(pl.col("t6"))
            .otherwise(pl.col("t0"))
            .alias("mother_annual_income")
        )

        father_income_expr = (
            pl.when(pl.col("relative_year") == 0)
            .then(pl.col("t0"))
            .when(pl.col("relative_year") == 1)
            .then(pl.col("t1"))
            .when(pl.col("relative_year") == 2)
            .then(pl.col("t2"))
            .when(pl.col("relative_year") == 3)
            .then(pl.col("t3"))
            .when(pl.col("relative_year") == 4)
            .then(pl.col("t4"))
            .when(pl.col("relative_year") == 5)
            .then(pl.col("t5"))
            .when(pl.col("relative_year") == 6)
            .then(pl.col("t6"))
            .otherwise(pl.col("t0"))
            .alias("father_annual_income")
        )

        mother_emp_expr = (
            pl.when(pl.col("relative_year") == 0)
            .then(pl.col("t0"))
            .when(pl.col("relative_year") == 1)
            .then(pl.col("t1"))
            .when(pl.col("relative_year") == 2)
            .then(pl.col("t2"))
            .when(pl.col("relative_year") == 3)
            .then(pl.col("t3"))
            .when(pl.col("relative_year") == 4)
            .then(pl.col("t4"))
            .when(pl.col("relative_year") == 5)
            .then(pl.col("t5"))
            .when(pl.col("relative_year") == 6)
            .then(pl.col("t6"))
            .otherwise(pl.col("t0"))
            .alias("mother_employment")
        )

        father_emp_expr = (
            pl.when(pl.col("relative_year") == 0)
            .then(pl.col("t0"))
            .when(pl.col("relative_year") == 1)
            .then(pl.col("t1"))
            .when(pl.col("relative_year") == 2)
            .then(pl.col("t2"))
            .when(pl.col("relative_year") == 3)
            .then(pl.col("t3"))
            .when(pl.col("relative_year") == 4)
            .then(pl.col("t4"))
            .when(pl.col("relative_year") == 5)
            .then(pl.col("t5"))
            .when(pl.col("relative_year") == 6)
            .then(pl.col("t6"))
            .otherwise(pl.col("t0"))
            .alias("father_employment")
        )

        # Add time-varying variables
        return joined_df.with_columns(
            [
                mother_income_expr,
                father_income_expr,
                mother_emp_expr,
                father_emp_expr,
            ]
        )

    def prepare_data(self, data_path: str) -> pl.DataFrame:
        df = pl.scan_parquet(data_path)

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

        # Calculate all required fields
        df = df.with_columns(
            [
                # Parent ages at birth
                (
                    pl.col("child_birthdate").dt.year()
                    - pl.col("mother_birthdate").dt.year()
                ).alias("mother_age_at_birth"),
                (
                    pl.col("child_birthdate").dt.year()
                    - pl.col("father_birthdate").dt.year()
                ).alias("father_age_at_birth"),
                # Treatment indicators
                pl.col("diagnosis_date").is_not_null().alias("treatment_status"),
                pl.col("diagnosis_date").alias("treatment_time"),
                # Epoch days for matching
                pl.col("child_birthdate").dt.epoch("d").alias("child_birth_days"),
                pl.col("mother_birthdate").dt.epoch("d").alias("mother_birth_days"),
                pl.col("father_birthdate").dt.epoch("d").alias("father_birth_days"),
                # Date differences for analysis
                (pl.col("child_birthdate") - pl.col("child_birthdate").shift())
                .dt.total_days()
                .alias("birth_date_diff"),
                (pl.col("mother_birthdate") - pl.col("mother_birthdate").shift())
                .dt.total_days()
                .alias("mother_birth_date_diff"),
                (pl.col("father_birthdate") - pl.col("father_birthdate").shift())
                .dt.total_days()
                .alias("father_birth_date_diff"),
            ]
        )

        # Normalize age variables
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
        """Find matches using vectorized operations with optimization"""
        # Identify treated and control cases
        treated_df = df.filter(pl.col("diagnosis_date").is_not_null())
        control_df = df.filter(pl.col("diagnosis_date").is_null())

        # Get fm_living status for treated cases
        treated_fm_living = self._get_fm_living_status(
            treated_df, reference_date_col="diagnosis_date"
        )

        # Create natural chunks based on fm_living and date constraints
        matches = []
        used_controls = set() if not self.allow_replacement else set()
        matched_treated = set()  # Keep track of treated cases that have been matched

        # Process each treated case with its natural control group
        for treated_idx in range(len(treated_df)):
            treated_case = treated_fm_living.slice(treated_idx, 1)
            treated_id = treated_case.get_column("pnr")[0]

            # Skip if this treated case has already been matched
            if treated_id in matched_treated:
                continue

            # Get the characteristics of the treated case
            fm_living_val = treated_case.get_column("fm_living")[0]
            child_birth = treated_case.get_column("child_birthdate")[0]
            mother_birth = treated_case.get_column("mother_birthdate")[0]
            father_birth = treated_case.get_column("father_birthdate")[0]
            diagnosis_date = treated_case.get_column("diagnosis_date")[0]

            # Add diagnosis date as a temporary column to control_df
            control_df_with_date = control_df.with_columns(
                pl.lit(diagnosis_date).alias("reference_date")
            )

            # Get fm_living status for controls at diagnosis time
            control_fm_living = self._get_fm_living_status(
                control_df_with_date, reference_date_col="reference_date"
            )

            # Filter controls based on natural grouping criteria
            available_controls = control_fm_living.filter(
                # Exact match on fm_living at diagnosis time
                (pl.col("fm_living") == fm_living_val)
                &
                # Date tolerances
                (
                    abs(pl.col("child_birthdate") - child_birth).dt.total_days()
                    <= self.child_date_tolerance
                )
                & (
                    abs(pl.col("mother_birthdate") - mother_birth).dt.total_days()
                    <= self.parent_date_tolerance
                )
                & (
                    abs(pl.col("father_birthdate") - father_birth).dt.total_days()
                    <= self.parent_date_tolerance
                )
            )

            # Remove already used controls if not allowing replacement
            if not self.allow_replacement:
                available_controls = available_controls.filter(
                    ~pl.col("pnr").cast(pl.Utf8).is_in(list(used_controls))
                )

            print(
                f"\n=== Processing treated case {treated_idx + 1} of {len(treated_df)} ==="
            )
            print(f"Treated ID: {treated_id}")
            print(f"FM Living: {fm_living_val}")
            print(f"Number of eligible controls: {len(available_controls)}")

            if len(available_controls) < 1:
                print("Warning: No eligible controls for this treated case")
                continue

            # Perform matching for this treated case and its eligible controls
            chunk_matches = self._match_chunk_optimized(
                treated_case, available_controls
            )

            if not chunk_matches.is_empty():
                matches.append(chunk_matches)
                matched_treated.add(treated_id)  # Mark this treated case as matched
                if not self.allow_replacement:
                    used_controls.update(
                        chunk_matches.get_column("control_id").to_list()
                    )
                    print(f"Total controls used so far: {len(used_controls)}")
                    print(f"Total treated matched so far: {len(matched_treated)}")

        return pl.concat(matches) if matches else self._empty_matches_df()

    def _get_eligible_controls(
        self, treated_chunk: pl.DataFrame, control_df: pl.DataFrame
    ) -> pl.DataFrame:
        """Get eligible controls based on exact matching criteria and time constraints"""
        filters = []

        # Exact matching criteria
        for col in self.exact_match_cols:
            unique_values = treated_chunk.get_column(col).unique()
            filters.append(pl.col(col).is_in(unique_values))

        # Time-based eligibility
        treatment_times = treated_chunk.get_column("treatment_time")
        filters.append(
            pl.col("treatment_time").is_null()
            | (pl.col("treatment_time") > treatment_times.max())
        )

        # Date tolerance filters
        filters.extend(
            [
                abs(
                    pl.col("child_birth_days")
                    - treated_chunk.get_column("child_birth_days").mean()
                )
                <= self.child_date_tolerance,
                abs(
                    pl.col("mother_birth_days")
                    - treated_chunk.get_column("mother_birth_days").mean()
                )
                <= self.parent_date_tolerance,
                abs(
                    pl.col("father_birth_days")
                    - treated_chunk.get_column("father_birth_days").mean()
                )
                <= self.parent_date_tolerance,
            ]
        )

        return control_df.filter(pl.all_horizontal(filters))

    def _calculate_mahalanobis_distance(
        self, treated_covs: np.ndarray, control_covs: np.ndarray
    ) -> np.ndarray:
        """Calculate Mahalanobis distance between treated and control covariates using vectorization"""
        # Validate input shapes
        if treated_covs.shape[1] != control_covs.shape[1]:
            raise ValueError(
                f"Treated and control covariates must have same number of features. "
                f"Got {treated_covs.shape[1]} and {control_covs.shape[1]}"
            )

        try:
            # Calculate covariance matrix using all data
            cov = np.cov(np.vstack([treated_covs, control_covs]).T)
            inv_cov = np.linalg.pinv(cov)  # Use pseudoinverse for numerical stability

            # Reshape arrays for broadcasting
            treated_expanded = treated_covs[:, np.newaxis, :]
            control_expanded = control_covs[np.newaxis, :, :]

            # Calculate differences
            diff = treated_expanded - control_expanded

            # Calculate Mahalanobis distances
            mahal_dist = np.sqrt(np.sum(np.matmul(diff, inv_cov) * diff, axis=2))

            return mahal_dist

        except np.linalg.LinAlgError:
            raise ValueError(
                "Failed to compute Mahalanobis distance: Covariance matrix is singular"
            )
        except Exception as e:
            raise ValueError(f"Failed to compute Mahalanobis distance: {str(e)}")

    def _match_chunk_optimized(
        self, treated: pl.DataFrame, controls: pl.DataFrame
    ) -> pl.DataFrame:
        """Perform matching using optimization with flexible number of matches"""
        if len(controls) < 1:
            print("Warning: No eligible controls available")
            return self._empty_matches_df()

        try:
            n_controls = len(controls)

            print("Optimization setup:")
            print(f"Number of eligible controls: {n_controls}")
            print(f"Maximum matches allowed: {self.n_matches}")

            # For a single treated case, we can simplify the matching
            if n_controls <= self.n_matches:
                # If we have fewer controls than requested matches, use all of them
                matches = []
                distances = self._calculate_mahalanobis_distance(
                    treated.select(self.match_vars).to_numpy(),
                    controls.select(self.match_vars).to_numpy(),
                )

                for j in range(n_controls):
                    matches.append(
                        {
                            "treated_id": treated.get_column("pnr")[0],
                            "control_id": controls.get_column("pnr")[j],
                            "treatment_time": treated.get_column("treatment_time")[0],
                            "distance": float(distances[0, j]),
                            # Add date differences
                            "birth_date_diff": abs(
                                treated.get_column("child_birth_days")[0]
                                - controls.get_column("child_birth_days")[j]
                            ),
                            "mother_birth_date_diff": abs(
                                treated.get_column("mother_birth_days")[0]
                                - controls.get_column("mother_birth_days")[j]
                            ),
                            "father_birth_date_diff": abs(
                                treated.get_column("father_birth_days")[0]
                                - controls.get_column("father_birth_days")[j]
                            ),
                        }
                    )

                return pl.DataFrame(matches)

            # If we have more controls than needed, use optimization to find best matches
            X = cp.Variable((1, n_controls), boolean=True)
            distances = self._calculate_mahalanobis_distance(
                treated.select(self.match_vars).to_numpy(),
                controls.select(self.match_vars).to_numpy(),
            )

            objective = cp.Minimize(cp.sum(cp.multiply(distances, X)))
            constraints = [
                cp.sum(X) <= self.n_matches,  # Maximum matches
                cp.sum(X) >= 1,  # At least one match
            ]

            prob = cp.Problem(objective, constraints)
            try:
                optimal_value = prob.solve(solver=cp.SCIP, verbose=False)
                print(f"Solver status: {prob.status}")
                print(f"Optimal value: {optimal_value}")
            except Exception as e:
                print(f"Solver error: {str(e)}")
                return self._empty_matches_df()

            if (
                prob.status not in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]
                or X.value is None
            ):
                print("Warning: No optimal solution found")
                return self._empty_matches_df()

            # Extract matches
            matches = []
            match_matrix = X.value > 0.5
            control_indices = np.where(match_matrix[0, :])[0]

            for j in control_indices:
                matches.append(
                    {
                        "treated_id": treated.get_column("pnr")[0],
                        "control_id": controls.get_column("pnr")[j],
                        "treatment_time": treated.get_column("treatment_time")[0],
                        "distance": float(distances[0, j]),
                        # Add date differences
                        "birth_date_diff": abs(
                            treated.get_column("child_birth_days")[0]
                            - controls.get_column("child_birth_days")[j]
                        ),
                        "mother_birth_date_diff": abs(
                            treated.get_column("mother_birth_days")[0]
                            - controls.get_column("mother_birth_days")[j]
                        ),
                        "father_birth_date_diff": abs(
                            treated.get_column("father_birth_days")[0]
                            - controls.get_column("father_birth_days")[j]
                        ),
                    }
                )

            return pl.DataFrame(matches)

        except Exception as e:
            print(f"Error in matching process: {str(e)}")
            return self._empty_matches_df()

    def evaluate_matches(
        self, matches: pl.DataFrame, original_df: pl.DataFrame
    ) -> Dict:
        """Evaluate matching results with combined metrics"""
        original_df = original_df.with_columns(pl.col("pnr").cast(pl.Utf8))

        # Get matched pairs
        matched_pairs = matches.join(
            original_df, left_on="treated_id", right_on="pnr"
        ).join(original_df, left_on="control_id", right_on="pnr", suffix="_control")

        # Compute balance statistics for static variables
        static_balance = self._compute_balance_statistics(
            matched_pairs, self.balance_check_vars["static"]
        )

        # Compute balance for time-varying variables before matching (birth date reference)
        birth_balance = self._compute_time_varying_balance(
            matched_pairs, self.balance_check_vars["time_varying"], "child_birthdate"
        )

        # Compute balance for time-varying variables after matching (treatment date reference)
        treatment_balance = self._compute_time_varying_balance(
            matched_pairs, self.balance_check_vars["time_varying"], "diagnosis_date"
        )

        return {
            "static_balance": static_balance,
            "birth_reference_balance": birth_balance,
            "treatment_reference_balance": treatment_balance,
            "summary": self._calculate_summary_stats(matches),
        }

    def _compute_standardized_differences(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        variables: List[str],
    ) -> pl.DataFrame:
        """
        Compute standardized differences between treated and control groups

        Args:
            treated_data: DataFrame containing treated group data
            control_data: DataFrame containing control group data
            variables: List of variable names to compute differences for
        """
        differences = []

        for var in variables:
            # Get values for both groups
            treated_values = treated_data.get_column(var).to_numpy()
            control_values = control_data.get_column(var).to_numpy()

            # Compute means
            treated_mean = np.mean(treated_values)
            control_mean = np.mean(control_values)

            # Compute pooled standard deviation
            treated_var = np.var(treated_values)
            control_var = np.var(control_values)
            pooled_sd = np.sqrt((treated_var + control_var) / 2)

            # Compute standardized difference
            std_diff = (
                (treated_mean - control_mean) / pooled_sd if pooled_sd != 0 else 0
            )

            differences.append(
                {
                    "variable": var,
                    "treated_mean": treated_mean,
                    "control_mean": control_mean,
                    "std_diff": std_diff,
                }
            )

        return pl.DataFrame(differences)

    def _compute_balance_statistics(
        self,
        matched_pairs: pl.DataFrame,
        variables: List[str],
        reference_date: Optional[str] = None,
    ) -> pl.DataFrame:
        """
        Compute balance statistics for variables (both static and time-varying)

        Args:
            matched_pairs: DataFrame containing matched pairs
            variables: List of variable names to compute balance for
            reference_date: Optional reference date for time-varying variables
        """

        def get_column_pairs(var: str) -> tuple[str, str]:
            if reference_date:
                treated_col = f"{var}_at_{reference_date}"
                control_col = f"{var}_at_{reference_date}_control"
            else:
                treated_col = var
                control_col = f"{var}_control"
            return treated_col, control_col

        # Create expressions for statistics calculation
        def make_balance_expr(var: str) -> List[pl.Expr]:
            treated_col, control_col = get_column_pairs(var)

            return [
                pl.lit(
                    treated_col if not reference_date else f"{var}_at_{reference_date}"
                ).alias("variable"),
                pl.col(treated_col).cast(pl.Float64).mean().alias("treated_mean"),
                pl.col(control_col).cast(pl.Float64).mean().alias("control_mean"),
                (
                    (
                        pl.col(treated_col).cast(pl.Float64).mean()
                        - pl.col(control_col).cast(pl.Float64).mean()
                    )
                    / (
                        (
                            pl.col(treated_col).cast(pl.Float64).std().pow(2)
                            + pl.col(control_col).cast(pl.Float64).std().pow(2)
                        )
                        / 2
                    ).sqrt()
                )
                .fill_null(0.0)
                .alias("std_diff"),
            ]

        # Compute statistics for all variables
        balance_stats = matched_pairs.select(
            pl.concat_list([make_balance_expr(var) for var in variables])
        ).fill_null(0.0)

        return balance_stats

    def _compute_time_varying_balance(
        self, matched_pairs: pl.DataFrame, variables: List[str], reference_date: str
    ) -> pl.DataFrame:
        """Compute balance statistics for time-varying variables"""
        return self._compute_balance_statistics(
            matched_pairs, variables, reference_date=reference_date
        )

    def plot_education_distribution(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        matches: Optional[pl.DataFrame] = None,
        save_path: Optional[str] = None,
    ):
        """
        Plot education level distribution before and after matching
        """
        with plt.style.context(["science", "ieee", "grid"]):
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))

            # Get education levels before matching
            treated_before = self._get_education_level(
                treated_data, reference_date_col="child_birthdate"
            )
            control_before = self._get_education_level(
                control_data, reference_date_col="child_birthdate"
            )

            # Plot mother's education before matching
            self._plot_education_dist(
                treated_before["mother_education"],
                control_before["mother_education"],
                axes[0, 0],
                "Mother's Education (Before Matching)",
            )

            # Plot father's education before matching
            self._plot_education_dist(
                treated_before["father_education"],
                control_before["father_education"],
                axes[0, 1],
                "Father's Education (Before Matching)",
            )

            if matches is not None:
                # Get education levels after matching
                matched_treated = matches.join(
                    treated_data, left_on="treated_id", right_on="pnr"
                )
                matched_control = matches.join(
                    control_data, left_on="control_id", right_on="pnr"
                )

                treated_after = self._get_education_level(
                    matched_treated, reference_date_col="diagnosis_date"
                )
                control_after = self._get_education_level(
                    matched_control, reference_date_col="diagnosis_date"
                )

                # Plot mother's education after matching
                self._plot_education_dist(
                    treated_after["mother_education"],
                    control_after["mother_education"],
                    axes[1, 0],
                    "Mother's Education (After Matching)",
                )

                # Plot father's education after matching
                self._plot_education_dist(
                    treated_after["father_education"],
                    control_after["father_education"],
                    axes[1, 1],
                    "Father's Education (After Matching)",
                )

            plt.tight_layout()

            if save_path:
                plt.savefig(
                    f"{save_path}_education_dist.pdf", dpi=300, bbox_inches="tight"
                )
                plt.close()
            else:
                plt.show()

    def _plot_education_dist(
        self, treated_edu: pl.Series, control_edu: pl.Series, ax: Axes, title: str
    ):
        """Helper function to plot education distribution"""
        edu_levels = list(range(1, 10))  # Convert range to list

        treated_counts = np.array(
            [(treated_edu == level).sum() / len(treated_edu) for level in edu_levels]
        )
        control_counts = np.array(
            [(control_edu == level).sum() / len(control_edu) for level in edu_levels]
        )

        x = np.arange(len(edu_levels))
        width = 0.35

        ax.bar(x - width / 2, treated_counts, width, label="Treated")
        ax.bar(x + width / 2, control_counts, width, label="Control")

        ax.set_xlabel("Education Level")
        ax.set_ylabel("Proportion")
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels([str(level) for level in edu_levels])  # Convert to strings
        ax.legend()

    def _calculate_summary_stats(self, matches: pl.DataFrame) -> Dict:
        """Calculate summary statistics"""
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

    def save_matches_to_csv(self, matches: pl.DataFrame, output_path: str) -> None:
        """
        Save basic matched pairs information to CSV file.

        Args:
            matches: DataFrame containing the matched pairs
            output_path: Path where to save the CSV file
        """
        if matches.is_empty():
            print("Warning: No matches to save")
            return

        # Select only essential matching columns
        basic_matches = matches.select(
            [
                "treated_id",
                "control_id",
                "treatment_time",
                "distance",
                "birth_date_diff",
                "mother_birth_date_diff",
                "father_birth_date_diff",
            ]
        )

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save to CSV
        basic_matches.write_csv(output_path)
        print(f"Matches saved to: {output_path}")

    def _compute_balance_statistics_for_groups(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        reference_date_col: str,
        id_col_treated: Optional[str] = None,
        id_col_control: Optional[str] = None,
    ) -> Dict[str, pl.DataFrame]:
        """
        Compute comprehensive balance statistics for treated and control groups

        Args:
            treated_data: DataFrame containing treated cases
            control_data: DataFrame containing control cases
            reference_date_col: Column name for reference date
            id_col_treated: Optional column name for treated ID (for matched data)
            id_col_control: Optional column name for control ID (for matched data)
        """
        balance_stats = {}

        # 1. Get education levels
        treated_with_edu = self._get_education_level(
            treated_data,
            reference_date_col=reference_date_col,
            id_col=id_col_treated if id_col_treated else "pnr",
        )
        control_with_edu = self._get_education_level(
            control_data,
            reference_date_col=reference_date_col,
            id_col=id_col_control if id_col_control else "pnr",
        )

        # Compute static balance statistics
        static_stats = self._compute_standardized_differences(
            treated_with_edu, control_with_edu, self.balance_check_vars["static"]
        )
        balance_stats["static"] = static_stats

        # 2. Get time-varying covariates
        treated_with_vars = self._get_time_varying_covariates(
            treated_with_edu,
            reference_date_col=reference_date_col,
            id_col=id_col_treated if id_col_treated else "pnr",
        )
        control_with_vars = self._get_time_varying_covariates(
            control_with_edu,
            reference_date_col=reference_date_col,
            id_col=id_col_control if id_col_control else "pnr",
        )

        # Compute time-varying balance statistics
        time_varying_stats = self._compute_standardized_differences(
            treated_with_vars,
            control_with_vars,
            self.balance_check_vars["time_varying"],
        )
        balance_stats["time_varying"] = time_varying_stats

        return balance_stats

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
            return self._empty_analysis_results()

        # Create analyzer instance with proper parameters
        analyzer = MatchingAnalyzer(
            data=original_df, matches=matches, education_hist=self.education_history
        )

        # Get matched treated and control data
        matched_treated = matches.join(
            original_df, left_on="treated_id", right_on="pnr"
        )
        matched_control = matches.join(
            original_df, left_on="control_id", right_on="pnr"
        )

        # Compute balance statistics
        balance_stats = self._compute_balance_statistics_for_groups(
            matched_treated,
            matched_control,
            reference_date_col="diagnosis_date",
            id_col_treated="treated_id",
            id_col_control="control_id",
        )

        # Generate visualizations and reports
        analyzer.plot_balance_diagnostics(
            balance_stats, save_path=f"{output_dir}/matching"
        )
        analyzer.plot_love_plot(balance_stats, save_path=f"{output_dir}/matching")
        analyzer.generate_summary_report(
            balance_stats, f"{output_dir}/matching_report.txt"
        )

        return {
            "match_stats": analyzer.compute_match_statistics(),
            "balance_stats": balance_stats,
        }

    def compute_comprehensive_balance_statistics(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        matches: Optional[pl.DataFrame] = None,
    ) -> Dict[str, Dict[str, pl.DataFrame]]:
        """Compute balance statistics for all variables including education"""
        # Compute balance statistics before matching
        before_stats = self._compute_balance_statistics_for_groups(
            treated_data, control_data, reference_date_col="child_birthdate"
        )

        balance_stats = {"before_matching": before_stats}

        # If matches provided, compute after-matching statistics
        if matches is not None:
            matched_treated = matches.join(
                treated_data, left_on="treated_id", right_on="pnr"
            )
            matched_control = matches.join(
                control_data, left_on="control_id", right_on="pnr"
            )

            after_stats = self._compute_balance_statistics_for_groups(
                matched_treated,
                matched_control,
                reference_date_col="diagnosis_date",
                id_col_treated="treated_id",
                id_col_control="control_id",
            )

            balance_stats["after_matching"] = after_stats

        return balance_stats

    def _empty_analysis_results(self) -> Dict:
        """Return empty analysis results structure"""
        return {
            "match_stats": {
                "n_treated": 0,
                "n_controls": 0,
                "avg_matches_per_treated": 0,
                "max_distance": 0,
                "mean_distance": 0,
                "median_distance": 0,
            },
            "balance_stats": {
                "static": pl.DataFrame(),
                "birth_reference": pl.DataFrame(),
                "treatment_reference": pl.DataFrame(),
            },
        }


class MatchingAnalyzer:
    def __init__(
        self, data: pl.DataFrame, matches: pl.DataFrame, education_hist: pl.LazyFrame
    ):
        self.original_data = data
        self.matches = matches
        self.treated_ids = matches.get_column("treated_id").unique()
        self.control_ids = matches.get_column("control_id").unique()
        self.education_history = (
            education_hist  # Add education_history as instance variable
        )

        # Set default plot style
        plt.style.use(["science", "ieee"])

    def compute_time_varying_balance(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        variables: List[str],
    ) -> pl.DataFrame:
        """Compute balance statistics for time-varying variables"""
        balance_stats = []

        for var in variables:
            if var not in treated_data.columns or var not in control_data.columns:
                print(f"Warning: Variable {var} not found in data")
                continue

            treated_vals = treated_data.get_column(var).to_numpy()
            control_vals = control_data.get_column(var).to_numpy()

            treated_mean = np.mean(treated_vals)
            treated_std = np.std(treated_vals)
            control_mean = np.mean(control_vals)
            control_std = np.std(control_vals)

            # Compute standardized difference
            pooled_std = np.sqrt((treated_std**2 + control_std**2) / 2)
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
        self, balance_stats: Dict[str, pl.DataFrame], save_path: Optional[str] = None
    ):
        """Create balance diagnostic plots"""
        for balance_type, stat_df in balance_stats.items():
            with plt.style.context(["science", "ieee", "grid"]):
                fig, ax = plt.subplots(figsize=(8, 6))

                data = stat_df.to_pandas()

                # Plot standardized differences
                sns.barplot(data=data, x="variable", y="std_diff", ax=ax)

                # Add reference lines
                ax.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
                ax.axhline(y=0.1, color="r", linestyle="--", linewidth=0.5)
                ax.axhline(y=-0.1, color="r", linestyle="--", linewidth=0.5)

                ax.set_xlabel("Variables")
                ax.set_ylabel("Standardized Difference")
                ax.set_title(f"Covariate Balance - {balance_type}")

                # Rotate x-axis labels for better readability
                plt.xticks(rotation=45, ha="right")

                plt.tight_layout()

                if save_path:
                    plt.savefig(
                        f"{save_path}_balance_{balance_type}.pdf",
                        dpi=300,
                        bbox_inches="tight",
                    )
                    plt.close()
                else:
                    plt.show()

    def compute_balance_statistics(self, variables: List[str]) -> pl.DataFrame:
        """Compute standardized differences for specified variables"""
        balance_stats = []

        treated_data = self.original_data.filter(pl.col("pnr").is_in(self.treated_ids))
        control_data = self.original_data.filter(pl.col("pnr").is_in(self.control_ids))

        for var in variables:
            # Convert to numpy array and then calculate stats to handle date/timedelta
            treated_vals = treated_data.get_column(var).to_numpy()
            control_vals = control_data.get_column(var).to_numpy()

            treated_mean = np.mean(treated_vals)
            treated_std = np.std(treated_vals)
            control_mean = np.mean(control_vals)
            control_std = np.std(control_vals)

            # Compute standardized difference
            pooled_std = np.sqrt((treated_std**2 + control_std**2) / 2)
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

    def generate_summary_report(
        self, balance_stats: Dict[str, pl.DataFrame], output_path: str
    ):
        """Generate a comprehensive matching summary report"""
        # Compute all statistics
        match_stats = self.compute_match_statistics()

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
            for group, stats in balance_stats.items():
                f.write(f"\n{group.title()} Variables:\n")
                f.write(stats.to_pandas().to_string())

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
                scipy_stats.probplot(treated_vals, dist="norm", plot=axes[idx])
                scipy_stats.probplot(control_vals, dist="norm", plot=axes[idx])

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
        self, balance_stats: Dict[str, pl.DataFrame], save_path: Optional[str] = None
    ):
        """Create a Love plot showing standardized differences before and after matching"""
        with plt.style.context(["science", "ieee", "grid"]):
            fig, ax = plt.subplots(figsize=(8, 10))

            all_data = []
            for balance_type, stats in balance_stats.items():
                df = stats.to_pandas()
                df["type"] = balance_type
                all_data.append(df)

            data = pd.concat(all_data)
            # Sort by absolute value of std_diff within each type
            data = data.sort_values(
                ["type", "std_diff"],
                key=lambda x: x if x.name != "std_diff" else x.abs(),
            )

            y_pos = np.arange(len(data))
            ax.barh(y_pos, data["std_diff"])

            ax.axvline(x=0, color="k", linestyle="-", linewidth=0.5)
            ax.axvline(x=0.1, color="r", linestyle="--", linewidth=0.5)
            ax.axvline(x=-0.1, color="r", linestyle="--", linewidth=0.5)

            ax.set_yticks(y_pos)
            ax.set_yticklabels(
                [f"{row['variable']} ({row['type']})" for _, row in data.iterrows()]
            )
            ax.set_xlabel("Standardized Difference")
            ax.set_title("Love Plot: Covariate Balance")

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_love_plot.pdf", dpi=300, bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    def plot_education_distributions(
        self,
        treated_data: pl.DataFrame,
        control_data: pl.DataFrame,
        time_points: List[str] = ["before", "after"],
        save_path: Optional[str] = None,
    ) -> None:
        """
        Plot education level distributions for treated and control groups

        Args:
            treated_data: DataFrame containing treated cases
            control_data: DataFrame containing control cases
            time_points: List of time points to plot ("before" and/or "after" matching)
            save_path: Optional path to save the plot
        """
        with plt.style.context(["science", "ieee", "grid"]):
            # Calculate number of rows based on time points
            n_rows = len(time_points)
            fig, axes = plt.subplots(n_rows, 2, figsize=(12, 6 * n_rows))

            # Make axes 2D if only one time point
            if n_rows == 1:
                axes = axes[np.newaxis, :]

            edu_labels = {
                1: "Primary",
                2: "Lower secondary",
                3: "Upper secondary",
                4: "Post-secondary",
                5: "Short-cycle tertiary",
                6: "Bachelor's",
                7: "Master's",
                8: "Doctoral",
                9: "Unknown",
            }

            for row, time_point in enumerate(time_points):
                # Get education data for the appropriate time point
                if time_point == "before":
                    ref_date = "child_birthdate"
                    title_suffix = "Before Matching"
                else:
                    ref_date = "diagnosis_date"
                    title_suffix = "After Matching"

                treated_edu = self._get_education_levels(treated_data, ref_date)
                control_edu = self._get_education_levels(control_data, ref_date)

                # Plot mother's education
                self._plot_education_dist(
                    treated_edu["mother_education"],
                    control_edu["mother_education"],
                    axes[row, 0],
                    f"Mother's Education ({title_suffix})",
                    edu_labels,
                )

                # Plot father's education
                self._plot_education_dist(
                    treated_edu["father_education"],
                    control_edu["father_education"],
                    axes[row, 1],
                    f"Father's Education ({title_suffix})",
                    edu_labels,
                )

            plt.tight_layout()

            if save_path:
                plt.savefig(
                    f"{save_path}_education_dist.pdf", dpi=300, bbox_inches="tight"
                )
                plt.close()
            else:
                plt.show()

    def _get_education_levels(
        self, data: pl.DataFrame, reference_date: str
    ) -> Dict[str, np.ndarray]:
        """Get education levels for a given reference date"""
        edu_data = self._get_education_level(data, reference_date_col=reference_date)
        return {
            "mother_education": edu_data["mother_education"].to_numpy(),
            "father_education": edu_data["father_education"].to_numpy(),
        }

    def _get_education_level(
        self,
        df: pl.DataFrame,
        reference_date_col: str,
        id_col: str = "pnr",  # Add id_col parameter with default value
    ) -> pl.DataFrame:
        """
        Get education level for parents at the reference date using LazyFrame

        Args:
            df: DataFrame containing the main data
            reference_date_col: Column name for reference date
            id_col: Column name containing the person identifier (default: "pnr")
        """
        # Convert reference dates from main dataframe to a column we can use for joining
        df_with_date = df.with_columns(
            [
                pl.col(reference_date_col).alias("reference_date"),
                pl.col(id_col).alias("pnr"),  # Create pnr column from id_col
            ]
        ).lazy()

        # Get latest education level before reference date for each parent
        education_levels = (
            self.education_history
            # Join with main data to get reference dates
            .join(df_with_date.select(["pnr", "reference_date"]), on="pnr", how="inner")
            # Filter for education records before reference date
            .filter(
                pl.col("date").cast(pl.Date) <= pl.col("reference_date").cast(pl.Date)
            )
            .group_by(["pnr", "type"])
            .agg([pl.col("education_level").last().alias("education_level")])
            # Group by pnr to get mother and father education in same row
            .group_by("pnr")
            .agg(
                [
                    pl.col("education_level")
                    .filter(pl.col("type") == "mother")
                    .max()
                    .alias("mother_education"),
                    pl.col("education_level")
                    .filter(pl.col("type") == "father")
                    .max()
                    .alias("father_education"),
                ]
            )
        )

        # Join with main data and handle missing values
        return df.join(
            education_levels.collect(),  # Convert to eager mode for joining
            left_on=id_col,  # Use id_col for joining
            right_on="pnr",
            how="left",
        ).with_columns(
            [
                # Fill missing values with 9 (Unknown/Missing)
                pl.col("mother_education").fill_null(9),
                pl.col("father_education").fill_null(9),
            ]
        )

    def _plot_education_dist(
        self,
        treated_edu: np.ndarray,
        control_edu: np.ndarray,
        ax: Axes,
        title: str,
        edu_labels: Dict[int, str],
    ) -> None:
        """
        Plot education distribution for a single group

        Args:
            treated_edu: Education levels for treated group
            control_edu: Education levels for control group
            ax: Matplotlib axis to plot on
            title: Plot title
            edu_labels: Dictionary mapping education codes to labels
        """
        edu_levels = sorted(edu_labels.keys())

        # Calculate proportions
        treated_props = np.array(
            [np.mean(treated_edu == level) for level in edu_levels]
        )
        control_props = np.array(
            [np.mean(control_edu == level) for level in edu_levels]
        )

        x = np.arange(len(edu_levels))
        width = 0.35

        # Create bars
        treated_bars = ax.bar(
            x - width / 2,
            treated_props,
            width,
            label="Treated",
            color="steelblue",
            alpha=0.7,
        )
        control_bars = ax.bar(
            x + width / 2,
            control_props,
            width,
            label="Control",
            color="lightcoral",
            alpha=0.7,
        )

        # Customize plot
        ax.set_ylabel("Proportion")
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(
            [edu_labels[level] for level in edu_levels], rotation=45, ha="right"
        )
        ax.legend()

        # Add value labels on bars
        self._add_value_labels(ax, treated_bars)
        self._add_value_labels(ax, control_bars)

        # Add grid
        ax.grid(True, axis="y", linestyle="--", alpha=0.7)

    def _add_value_labels(self, ax: Axes, bars: Container) -> None:
        """Add value labels on top of bars"""
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.2%}",
                ha="center",
                va="bottom",
                rotation=0,
                fontsize=8,
            )


def main():
    config = {
        "n_matches": 10,
        "child_date_tolerance": 30,  # 30 days for child
        "parent_date_tolerance": 365.25,  # 1 year for parents
        "allow_replacement": False,
        "income_history_path": "data/income_history.parquet",
        "employment_history_path": "data/employment_history.parquet",
        "fm_living_history_path": "data/fm_living_history.parquet",
        "education_history_path": "data/education_history.parquet",
    }

    print("Starting matching process...")
    matcher = VectorizedRiskSetMatcher(config)

    print("Loading data...")
    df = matcher.prepare_data("data/test_data.csv")

    print("Finding matches...")
    matches = matcher.find_matches(df)

    print("Saving detailed matches to CSV...")
    matcher.save_matches_to_csv(matches, "output/matched_pairs.csv")

    print("\nGenerating analysis and plots...")
    analysis_results = matcher.analyze_matches(matches, df, output_dir="output")

    # Create analyzer with education history
    analyzer = MatchingAnalyzer(
        data=df, matches=matches, education_hist=matcher.education_history
    )

    analyzer.plot_education_distributions(
        treated_data=df.filter(pl.col("diagnosis_date").is_not_null()),
        control_data=df.filter(pl.col("diagnosis_date").is_null()),
        time_points=["before", "after"],
        save_path="output/matching",
    )

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
