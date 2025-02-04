from typing import Dict, List, Optional

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
import seaborn as sns
from scipy import stats


class MatchingAnalyzer:
    def __init__(self, original_data: pl.DataFrame, matches: pl.DataFrame):
        self.original_data = original_data
        self.matches = matches
        self.treated_ids = matches.get_column("treated_id").unique()
        self.control_ids = matches.get_column("control_id").unique()

        # Set default plot style
        plt.style.use(['science', 'ieee'])

    def compute_match_statistics(self) -> Dict:
            """Compute basic matching statistics"""
            stats = {
                "n_treated": len(self.treated_ids),
                "n_controls": len(self.control_ids),
                "avg_matches_per_treated": len(self.matches) / len(self.treated_ids),
                "max_distance": self.matches.get_column("distance").max(),
                "mean_distance": self.matches.get_column("distance").mean(),
                "median_distance": self.matches.get_column("distance").median(),
            }

            # Date difference statistics
            for diff_col in ["birth_date_diff", "mother_birth_date_diff", "father_birth_date_diff"]:
                stats[f"{diff_col}_mean"] = self.matches.get_column(diff_col).mean()
                stats[f"{diff_col}_max"] = self.matches.get_column(diff_col).max()

            return stats

    def plot_distance_distribution(self, save_path: Optional[str] = None):
        """Plot the distribution of matching distances"""
        with plt.style.context(['science', 'ieee']):
            fig, ax = plt.subplots(figsize=(6, 4))

            data = self.matches.to_pandas()
            sns.histplot(data=data, x="distance", bins=30, ax=ax)

            ax.set_xlabel("Matching Distance")
            ax.set_ylabel("Count")
            ax.set_title("Distribution of Matching Distances")

            if save_path:
                plt.savefig(f"{save_path}_distances.pdf", dpi=300, bbox_inches='tight')
                plt.close()
            else:
                plt.show()

    def plot_date_differences(self, save_path: Optional[str] = None):
        """Plot the distribution of date differences"""
        with plt.style.context(['science', 'ieee', 'grid']):
            fig, axes = plt.subplots(1, 3, figsize=(12, 4))

            date_cols = ["birth_date_diff", "mother_birth_date_diff", "father_birth_date_diff"]
            titles = ["Birth Date", "Mother Birth Date", "Father Birth Date"]

            data = self.matches.to_pandas()

            for ax, col, title in zip(axes, date_cols, titles):
                sns.boxplot(data=data, y=col, ax=ax)
                ax.set_title(title)
                ax.set_ylabel("Days")

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_date_diffs.pdf", dpi=300, bbox_inches='tight')
                plt.close()
            else:
                plt.show()

    def plot_balance_diagnostics(self, balance_stats: pl.DataFrame, save_path: Optional[str] = None):
        """Create balance diagnostic plots"""
        with plt.style.context(['science', 'ieee', 'grid']):
            fig, ax = plt.subplots(figsize=(8, 6))

            data = balance_stats.to_pandas()

            # Plot standardized differences
            sns.barplot(data=data, x="variable", y="std_diff", ax=ax)

            # Add reference lines
            ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
            ax.axhline(y=0.1, color='r', linestyle='--', linewidth=0.5)
            ax.axhline(y=-0.1, color='r', linestyle='--', linewidth=0.5)

            ax.set_xlabel("Variables")
            ax.set_ylabel("Standardized Difference")
            ax.set_title("Covariate Balance")

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45, ha='right')

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_balance.pdf", dpi=300, bbox_inches='tight')
                plt.close()
            else:
                plt.show()

    def compute_balance_statistics(self, variables: List[str]) -> pl.DataFrame:
            """Compute standardized differences for specified variables"""
            balance_stats = []

            treated_data = self.original_data.filter(
                pl.col("subject_id").is_in(self.treated_ids)
            )
            control_data = self.original_data.filter(
                pl.col("subject_id").is_in(self.control_ids)
            )

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
                std_diff = ((treated_mean - control_mean) / pooled_std
                          if pooled_std != 0 else 0)

                balance_stats.append({
                    "variable": var,
                    "treated_mean": float(treated_mean),
                    "control_mean": float(control_mean),
                    "std_diff": float(std_diff),
                })

            return pl.DataFrame(balance_stats)


    def generate_summary_report(self, variables: List[str], output_path: str):
        """Generate a comprehensive matching summary report"""
        # Compute all statistics
        match_stats = self.compute_match_statistics()
        balance_stats = self.compute_balance_statistics(variables)

        # Create report
        with open(output_path, 'w') as f:
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
        with plt.style.context(['science', 'ieee', 'grid']):
            n_vars = len(variables)
            n_cols = 3
            n_rows = (n_vars + n_cols - 1) // n_cols

            fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4*n_rows))
            axes = axes.ravel()

            treated_data = self.original_data.filter(
                pl.col("subject_id").is_in(self.treated_ids)
            )
            control_data = self.original_data.filter(
                pl.col("subject_id").is_in(self.control_ids)
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
                plt.savefig(f"{save_path}_qq_plots.pdf", dpi=300, bbox_inches='tight')
                plt.close()
            else:
                plt.show()

    def plot_love_plot(self, balance_stats: pl.DataFrame, save_path: Optional[str] = None):
        """Create a Love plot showing standardized differences before and after matching"""
        with plt.style.context(['science', 'ieee', 'grid']):
            fig, ax = plt.subplots(figsize=(8, len(balance_stats)*0.3))

            data = balance_stats.to_pandas()

            # Sort by absolute standardized difference
            data = data.sort_values('std_diff', key=abs)

            # Create horizontal bar plot
            y_pos = np.arange(len(data))
            ax.barh(y_pos, data['std_diff'])

            # Add reference lines
            ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
            ax.axvline(x=0.1, color='r', linestyle='--', linewidth=0.5)
            ax.axvline(x=-0.1, color='r', linestyle='--', linewidth=0.5)

            # Customize plot
            ax.set_yticks(y_pos)
            ax.set_yticklabels(data['variable'])
            ax.set_xlabel('Standardized Difference')
            ax.set_title('Love Plot: Covariate Balance')

            plt.tight_layout()

            if save_path:
                plt.savefig(f"{save_path}_love_plot.pdf", dpi=300, bbox_inches='tight')
                plt.close()
            else:
                plt.show()


# Example usage (commented out since variables are undefined)
# analyzer = MatchingAnalyzer(original_data, matches)
# variables = ["age", "income", "education"]
# balance_stats = analyzer.compute_balance_statistics(variables)

# Create output directory
import os

os.makedirs("output", exist_ok=True)

# Example plotting calls (commented out since analyzer is undefined)
# analyzer.plot_distance_distribution(save_path="output/matching")
# analyzer.plot_date_differences(save_path="output/matching")
# analyzer.plot_balance_diagnostics(balance_stats, save_path="output/matching")
# analyzer.plot_qq_plots(variables, save_path="output/matching")
# analyzer.plot_love_plot(balance_stats, save_path="output/matching")
