import numpy as np
import pandas as pd
import polars as pl


def generate_time_varying_data(main_data_path: str, output_dir: str = "data"):
    """
    Generate time-varying covariate data based on the main dataset
    """
    # Read main data
    df = pl.read_csv(main_data_path)

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate income history
    def generate_income_history(row_count: int, parent_type: str):
        # Base income parameters
        if parent_type == "mother":
            base_mean = 350000
            base_std = 50000
        else:  # father
            base_mean = 400000
            base_std = 60000

        # Generate base income for each person
        base_incomes = np.random.normal(base_mean, base_std, row_count)

        # Generate yearly variations (with trend and random component)
        yearly_data = []
        for pnr in range(row_count):
            # Individual trend (between 1-4% yearly increase)
            trend = np.random.uniform(0.01, 0.04)

            # Generate 7 years of data (t_0 to t_6)
            income_trajectory = []
            base = base_incomes[pnr]

            for year in range(7):
                # Add trend and random variation
                income = base * (1 + trend * year) * (1 + np.random.normal(0, 0.05))
                income_trajectory.append(round(max(0, income)))  # Ensure non-negative

            yearly_data.append(income_trajectory)

        return yearly_data

    # Generate employment history
    def generate_employment_history(row_count: int, parent_type: str):
        # Employment status parameters (probability of being employed)
        if parent_type == "mother":
            base_prob = 0.85
        else:  # father
            base_prob = 0.90

        # Generate yearly employment status
        yearly_data = []
        for pnr in range(row_count):
            # Individual employment probability
            prob = np.random.beta(10, 2) * base_prob

            # Generate 7 years of data (t_0 to t_6)
            employment_trajectory = []

            # Initial status
            status = np.random.binomial(1, prob)

            for year in range(7):
                if status == 1:
                    # If employed, high probability of staying employed
                    status = np.random.binomial(1, 0.95)
                else:
                    # If unemployed, moderate probability of finding employment
                    status = np.random.binomial(1, 0.3)

                employment_trajectory.append(status)

            yearly_data.append(employment_trajectory)

        return yearly_data

    # Generate data for both parents
    n_families = len(df)

    # Income history
    mother_income = generate_income_history(n_families, "mother")
    father_income = generate_income_history(n_families, "father")

    # Employment history
    mother_employment = generate_employment_history(n_families, "mother")
    father_employment = generate_employment_history(n_families, "father")

    # Create income history DataFrame
    income_data = []
    for idx in range(n_families):
        # Mother's income
        income_data.append(
            {
                "pnr": df["pnr"][idx],
                "type": "mother",
                "t_0": mother_income[idx][0],
                "t_1": mother_income[idx][1],
                "t_2": mother_income[idx][2],
                "t_3": mother_income[idx][3],
                "t_4": mother_income[idx][4],
                "t_5": mother_income[idx][5],
                "t_6": mother_income[idx][6],
            }
        )
        # Father's income
        income_data.append(
            {
                "pnr": df["pnr"][idx],
                "type": "father",
                "t_0": father_income[idx][0],
                "t_1": father_income[idx][1],
                "t_2": father_income[idx][2],
                "t_3": father_income[idx][3],
                "t_4": father_income[idx][4],
                "t_5": father_income[idx][5],
                "t_6": father_income[idx][6],
            }
        )

    # Create employment history DataFrame
    employment_data = []
    for idx in range(n_families):
        # Mother's employment
        employment_data.append(
            {
                "pnr": df["pnr"][idx],
                "type": "mother",
                "t_0": mother_employment[idx][0],
                "t_1": mother_employment[idx][1],
                "t_2": mother_employment[idx][2],
                "t_3": mother_employment[idx][3],
                "t_4": mother_employment[idx][4],
                "t_5": mother_employment[idx][5],
                "t_6": mother_employment[idx][6],
            }
        )
        # Father's employment
        employment_data.append(
            {
                "pnr": df["pnr"][idx],
                "type": "father",
                "t_0": father_employment[idx][0],
                "t_1": father_employment[idx][1],
                "t_2": father_employment[idx][2],
                "t_3": father_employment[idx][3],
                "t_4": father_employment[idx][4],
                "t_5": father_employment[idx][5],
                "t_6": father_employment[idx][6],
            }
        )

    # Convert to Polars DataFrames
    income_df = pl.DataFrame(income_data)
    employment_df = pl.DataFrame(employment_data)

    # Save to CSV
    income_df.write_csv(f"{output_dir}/income_history.csv")
    employment_df.write_csv(f"{output_dir}/employment_history.csv")

    return income_df, employment_df


def generate_fm_living_history(main_data_path: str, output_dir: str = "data"):
    """
    Generate family living arrangement history

    Categories:
    1 = Both parents
    2 = Mother only
    3 = Father only
    4 = Mother and partner
    5 = Father and partner
    6 = Other arrangement
    """
    # Read main data
    df = pl.read_csv(main_data_path)

    # Set random seed for reproducibility
    np.random.seed(42)

    def generate_fm_living_trajectory():
        """Generate a realistic trajectory of living arrangements"""
        # Start with initial living arrangement
        # Higher probability of starting with both parents
        initial_probs = [
            0.8,
            0.1,
            0.02,
            0.05,
            0.02,
            0.01,
        ]  # probabilities for categories 1-6
        initial_state = np.random.choice(range(1, 7), p=initial_probs)

        # Transition probabilities matrix (simplified example)
        # Rows: current state, Columns: next state
        transition_probs = {
            1: [
                0.95,
                0.02,
                0.01,
                0.01,
                0.005,
                0.005,
            ],  # High probability of staying with both parents
            2: [
                0.05,
                0.80,
                0.02,
                0.10,
                0.02,
                0.01,
            ],  # High probability of staying with mother
            3: [
                0.05,
                0.02,
                0.80,
                0.02,
                0.10,
                0.01,
            ],  # High probability of staying with father
            4: [
                0.05,
                0.10,
                0.02,
                0.80,
                0.02,
                0.01,
            ],  # High probability of staying with mother+partner
            5: [
                0.05,
                0.02,
                0.10,
                0.02,
                0.80,
                0.01,
            ],  # High probability of staying with father+partner
            6: [
                0.10,
                0.20,
                0.20,
                0.20,
                0.20,
                0.10,
            ],  # More volatile transitions from other arrangements
        }

        trajectory = [initial_state]

        # Generate subsequent states
        for _ in range(6):  # t_1 to t_6
            current_state = trajectory[-1]
            next_state = np.random.choice(
                range(1, 7), p=transition_probs[current_state]
            )
            trajectory.append(next_state)

        return trajectory

    # Generate fm_living history for each family
    fm_living_data = []
    for idx in range(len(df)):
        trajectory = generate_fm_living_trajectory()
        fm_living_data.append(
            {
                "pnr": df["pnr"][idx],
                "t_0": trajectory[0],
                "t_1": trajectory[1],
                "t_2": trajectory[2],
                "t_3": trajectory[3],
                "t_4": trajectory[4],
                "t_5": trajectory[5],
                "t_6": trajectory[6],
            }
        )

    # Convert to Polars DataFrame
    fm_living_df = pl.DataFrame(fm_living_data)

    # Save to CSV
    fm_living_df.write_csv(f"{output_dir}/fm_living_history.csv")

    return fm_living_df


def generate_education_history(main_data_path: str, output_dir: str = "data"):
    """
    Generate education history data

    Education levels:
    1 = Primary education (lower level)
    2 = Primary education (upper level)
    3 = High school (gymnasium)
    4 = Vocational education
    5 = Short-cycle higher education
    6 = Bachelor's degree
    7 = Master's degree
    8 = PhD
    9 = Unknown/Missing
    """
    # Read main data
    df = pl.read_csv(main_data_path)

    # Set random seed for reproducibility
    np.random.seed(42)

    def generate_education_trajectory(birth_date, is_mother: bool):
        """
        Generate a realistic trajectory of education levels for an individual

        Args:
            birth_date: Individual's birth date
            is_mother: Boolean indicating if the individual is a mother
        """
        # Convert birth_date to datetime if it's a string
        if isinstance(birth_date, str):
            birth_date = pd.to_datetime(birth_date)

        # Education level probabilities (slightly different for mothers and fathers)
        if is_mother:
            level_probs = [0.05, 0.10, 0.20, 0.25, 0.15, 0.15, 0.08, 0.01, 0.01]
        else:
            level_probs = [0.07, 0.13, 0.15, 0.30, 0.12, 0.12, 0.09, 0.01, 0.01]

        # Determine highest education level
        max_level = np.random.choice(range(1, 10), p=level_probs)

        # Generate trajectory
        trajectory = []
        current_date = birth_date

        # Always start with level 1 (primary education lower level)
        trajectory.append(
            {
                "education_level": 1,
                "date": current_date + pd.DateOffset(years=7),  # Start school at age 7
            }
        )

        if max_level > 1:
            # Add level 2 (primary education upper level)
            trajectory.append(
                {
                    "education_level": 2,
                    "date": current_date
                    + pd.DateOffset(years=15),  # Complete at age 15
                }
            )

        if max_level > 2:
            # Determine path: high school (3) or vocational (4)
            if (
                max_level == 4 or np.random.random() < 0.4
            ):  # 40% chance of vocational if going further
                trajectory.append(
                    {
                        "education_level": 4,
                        "date": current_date
                        + pd.DateOffset(years=18, months=np.random.randint(0, 12)),
                    }
                )
            else:
                trajectory.append(
                    {
                        "education_level": 3,
                        "date": current_date
                        + pd.DateOffset(years=18, months=np.random.randint(0, 6)),
                    }
                )

        if max_level > 4:
            # Higher education
            if max_level == 5:
                # Short-cycle higher education
                trajectory.append(
                    {
                        "education_level": 5,
                        "date": current_date
                        + pd.DateOffset(years=20, months=np.random.randint(0, 12)),
                    }
                )
            elif max_level >= 6:
                # Bachelor's degree
                trajectory.append(
                    {
                        "education_level": 6,
                        "date": current_date
                        + pd.DateOffset(years=21, months=np.random.randint(0, 12)),
                    }
                )

                if max_level >= 7:
                    # Master's degree
                    trajectory.append(
                        {
                            "education_level": 7,
                            "date": current_date
                            + pd.DateOffset(years=23, months=np.random.randint(0, 12)),
                        }
                    )

                    if max_level == 8:
                        # PhD
                        trajectory.append(
                            {
                                "education_level": 8,
                                "date": current_date
                                + pd.DateOffset(
                                    years=27, months=np.random.randint(0, 24)
                                ),
                            }
                        )

        return trajectory

    # Generate education history for all parents
    education_data = []

    for idx in range(len(df)):
        # Mother's education
        mother_trajectory = generate_education_trajectory(
            df["mother_birthdate"][idx], is_mother=True
        )
        for level_data in mother_trajectory:
            education_data.append(
                {
                    "pnr": df["pnr"][idx],
                    "type": "mother",
                    "education_level": level_data["education_level"],
                    "date": level_data["date"].strftime("%Y-%m-%d"),
                }
            )

        # Father's education
        father_trajectory = generate_education_trajectory(
            df["father_birthdate"][idx], is_mother=False
        )
        for level_data in father_trajectory:
            education_data.append(
                {
                    "pnr": df["pnr"][idx],
                    "type": "father",
                    "education_level": level_data["education_level"],
                    "date": level_data["date"].strftime("%Y-%m-%d"),
                }
            )

    # Convert to Polars DataFrame
    education_df = pl.DataFrame(education_data)

    # Sort by pnr, type, and date
    education_df = education_df.sort(["pnr", "type", "date"])

    # Save to CSV
    education_df.write_csv(f"{output_dir}/education_history.csv")

    # Print some summary statistics
    print("\nEducation History Summary:")
    print(education_df.head(10))

    print("\nEducation Level Distribution by Parent Type:")
    summary = (
        education_df.group_by(["type", "education_level"])
        .agg(pl.count("pnr").alias("count"))
        .sort(["type", "education_level"])
    )
    print(summary)

    return education_df


if __name__ == "__main__":
    # Generate the time-varying covariate data
    income_df, employment_df = generate_time_varying_data(
        main_data_path="data/test_data.csv", output_dir="data"
    )

    # Generate the family living arrangement history
    fm_living_df = generate_fm_living_history(
        main_data_path="data/test_data.csv", output_dir="data"
    )

    # Generate education history
    education_df = generate_education_history(
        main_data_path="data/test_data.csv", output_dir="data"
    )

    # Print some summary statistics
    print("\nIncome History Summary:")
    print(income_df.head())
    print("\nEmployment History Summary:")
    print(employment_df.head())

    # Print some basic statistics
    print("\nIncome Statistics:")
    for year in range(7):
        col = f"t_{year}"
        print(f"\n{col}:")
        stats = income_df.select(
            [
                pl.col(col).mean().alias("mean"),
                pl.col(col).std().alias("std"),
                pl.col(col).min().alias("min"),
                pl.col(col).max().alias("max"),
                pl.col(col).median().alias("median"),
            ]
        )
        print(stats)

    print("\nEmployment Statistics:")
    for year in range(7):
        col = f"t_{year}"
        print(f"\n{col}:")
        stats = employment_df.select(
            [
                pl.col(col).mean().alias("mean"),
                pl.col(col).sum().alias("total_employed"),
                pl.col(col).count().alias("total_count"),
                (pl.col(col).mean() * 100).alias("employment_rate_%"),
            ]
        )
        print(stats)

    # You can also add group statistics by parent type
    print("\nIncome Statistics by Parent Type:")
    for year in range(7):
        col = f"t_{year}"
        print(f"\n{col}:")
        stats = income_df.group_by("type").agg(
            [
                pl.col(col).mean().alias("mean"),
                pl.col(col).std().alias("std"),
                pl.col(col).min().alias("min"),
                pl.col(col).max().alias("max"),
            ]
        )
        print(stats)
