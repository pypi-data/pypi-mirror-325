import glob
import os
import re
from typing import List

import polars as pl

OUTPUT_DIR = "output_data"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def get_child_parent_relationships(
    relationship_file_path: str, filter_file_path: str
) -> pl.LazyFrame:
    """Get filtered child-parent relationships using lazy evaluation."""
    relationships = pl.scan_parquet(relationship_file_path).select(
        [pl.col("PNR"), pl.col("FAR_ID"), pl.col("MOR_ID")]
    )

    filter_df = pl.scan_parquet(filter_file_path).select(pl.col("PNR"))

    return relationships.join(filter_df, on="PNR", how="inner").select(
        [
            pl.col("PNR").alias("child_pnr"),
            pl.col("FAR_ID").alias("father_pnr"),
            pl.col("MOR_ID").alias("mother_pnr"),
        ]
    )


def get_parquet_files(directory: str) -> List[str]:
    """Get all parquet files in directory."""
    return glob.glob(os.path.join(directory, "**/*.parquet"), recursive=True)


def get_year_from_filename(filename: str) -> int:
    """Extract year from filename."""
    return int("".join(filter(str.isdigit, os.path.basename(filename)))[:4])


def get_date_from_filename(filename: str) -> tuple[int, int]:
    """
    Extract year and month from filename in format yyyymm.

    Args:
        filename: Filename in format yyyymm

    Returns:
        Tuple of (year, month)
    """
    match = re.search(r"(\d{4})(\d{2})", os.path.basename(filename))
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        return year, month
    raise ValueError(f"Invalid filename format: {filename}")


def get_birth_years() -> pl.LazyFrame:
    """Get birth years for all children using lazy evaluation."""
    bef_files = get_parquet_files("registers/bef/")

    # Create lazy frames for each file and combine them
    birth_dfs = []

    for file in bef_files:
        year, month = get_date_from_filename(file)

        # For annual data (typically December) or quarterly data
        if month == 12 or month in [3, 6, 9]:
            df = (
                pl.scan_parquet(file)
                .select(["PNR", "FOED_DAG"])
                .with_columns(
                    [
                        pl.col("FOED_DAG")
                        .str.strptime(pl.Date, format="%d/%m/%Y")
                        .alias("birth_date")
                    ]
                )
            )
            birth_dfs.append(df)

    return (
        pl.concat(birth_dfs)
        .unique()
        .with_columns([pl.col("birth_date").dt.year().alias("birth_year")])
        .select(["PNR", "birth_year"])
    )


def create_time_periods(
    df: pl.LazyFrame, birth_year_col: str, data_year: int | str | pl.Expr
) -> pl.LazyFrame:
    """
    Create time period columns relative to birth year.

    Args:
        df: Input LazyFrame
        birth_year_col: Column name containing birth year
        data_year: Year value, column name, or polars expression
    """
    if isinstance(data_year, (int, str)):
        year_expr = (
            pl.col(data_year) if isinstance(data_year, str) else pl.lit(data_year)
        )
    else:
        year_expr = data_year

    return df.with_columns(
        [(year_expr - pl.col(birth_year_col)).alias("t_period")]
    ).filter((pl.col("t_period") >= 0) & (pl.col("t_period") <= 6))


def process_parent_data(
    df: pl.LazyFrame,
    child_parent: pl.LazyFrame,
    birth_years_df: pl.LazyFrame,
    parent_type: str,
    value_col: str,
    year: int | None = None,
) -> pl.LazyFrame:
    """
    Process data for a parent (mother or father).

    Args:
        df: Input LazyFrame
        child_parent: Child-parent relationships LazyFrame
        birth_years_df: Birth years LazyFrame
        parent_type: Type of parent ('mother' or 'father')
        value_col: Name of the value column to process
        year: Optional year value
    """
    parent_col = f"{parent_type}_pnr"

    joined = df.join(child_parent, left_on="PNR", right_on=parent_col).join(
        birth_years_df, left_on="child_pnr", right_on="PNR"
    )

    if year is not None:
        joined = create_time_periods(joined, "birth_year", pl.lit(year))
    else:
        joined = create_time_periods(joined, "birth_year", "attainment_year")

    return joined.select(
        [
            pl.col("child_pnr").alias("pnr"),
            pl.lit(parent_type).alias("type"),
            pl.col(value_col),
            pl.col("t_period"),
        ]
    )


def read_sas_format_file(file_path: str) -> dict[str, str]:
    """
    Read SAS format file and extract HDAUDD to ISCED level mapping.

    Args:
        file_path: Path to SAS format file

    Returns:
        Dictionary mapping HDAUDD codes to ISCED levels
    """
    mapping = {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Skip lines until we find the value statement
        start_idx = next(
            i for i, line in enumerate(lines) if "value AUDD_LEVEL_L1L4_K" in line
        )

        # Process mapping lines
        for line in lines[start_idx + 1 :]:
            line = line.strip()

            # Stop when we reach the end of the format
            if line.startswith(";"):
                break

            # Parse mapping line
            if "='" in line:
                hdaudd, isced = line.split("='")
                isced = isced.strip("'")
                mapping[hdaudd.strip()] = isced.strip()

    except Exception as e:
        print(f"Error reading SAS format file: {e}")
        raise

    return mapping


def create_education_history(child_parent: pl.LazyFrame, birth_years_df: pl.LazyFrame):
    """Create education history using lazy evaluation."""
    education_files = get_parquet_files("registers/uddf/")

    # Read HDAUDD to ISCED mapping
    isced_mapping = read_sas_format_file(
        r"\\srvfsenas1\data\Formater\SAS formater i Danmarks Statistik\HTML_oversigter\Disced\AUDD_LEVEL_L1L4_K.sas"
    )

    dfs = []
    for file in education_files:
        df = (
            pl.scan_parquet(file)
            .select(["PNR", "HFAUDD", "HF_VFRA"])
            .with_columns(
                [
                    pl.col("HFAUDD")
                    .cast(pl.Utf8)
                    .replace_strict(isced_mapping, default="9")
                    .alias("education_level"),
                    pl.col("HF_VFRA")
                    .str.strptime(pl.Date, format="%d/%m/%Y")
                    .dt.year()
                    .alias("attainment_year"),
                ]
            )
        )

        for parent_type in ["mother", "father"]:
            parent_df = process_parent_data(
                df, child_parent, birth_years_df, parent_type, "education_level"
            )
            dfs.append(parent_df)

    final_df = pl.concat(dfs).collect().unique()
    final_df.write_parquet(os.path.join(OUTPUT_DIR, "education_history.parquet"))


def create_historical_data(
    register_path: str,
    value_col: str,
    output_name: str,
    child_parent: pl.LazyFrame,
    birth_years_df: pl.LazyFrame,
):
    """Generic function to create historical data (income and socioeconomic status)."""
    files = get_parquet_files(register_path)

    dfs = []
    for file in files:
        year = get_year_from_filename(file)
        df = pl.scan_parquet(file).select(["PNR", value_col])

        for parent_type in ["mother", "father"]:
            parent_df = process_parent_data(
                df, child_parent, birth_years_df, parent_type, value_col, year
            )
            dfs.append(parent_df)

    final_df = (
        pl.concat(dfs)
        .collect()
        .pivot(
            values=value_col,
            index=["pnr", "type"],
            columns="t_period",
            aggregate_function="first",
        )
        .with_columns([pl.col(str(i)).alias(f"t{i}") for i in range(7)])
    )

    final_df.write_parquet(os.path.join(OUTPUT_DIR, output_name))


def create_family_arrangement(child_parent: pl.LazyFrame, birth_years_df: pl.LazyFrame):
    """Create family arrangement using lazy evaluation."""
    bef_files = get_parquet_files("registers/bef/")

    dfs = []
    for file in bef_files:
        year, month = get_date_from_filename(file)

        # Only process December (annual) or quarterly data
        if month == 12 or month in [3, 6, 9]:
            df = pl.scan_parquet(file).select(["PNR", "FM_MARK"])

            family_arr = df.join(
                child_parent, left_on="PNR", right_on="child_pnr"
            ).join(birth_years_df, left_on="child_pnr", right_on="PNR")

            family_arr = create_time_periods(family_arr, "birth_year", pl.lit(year))
            family_arr = family_arr.select(
                [
                    pl.col("child_pnr").alias("pnr"),
                    pl.col("FM_MARK"),
                    pl.col("t_period"),
                ]
            )

            dfs.append(family_arr)

    final_df = (
        pl.concat(dfs)
        .collect()
        .pivot(
            values="FM_MARK",
            index="pnr",
            columns="t_period",
            aggregate_function="first",
        )
        .with_columns([pl.col(str(i)).alias(f"t{i}") for i in range(7)])
    )

    final_df.write_parquet(os.path.join(OUTPUT_DIR, "fm_living_history.parquet"))


if __name__ == "__main__":
    print(f"Creating output directory: {OUTPUT_DIR}")

    # Get filtered child-parent relationships
    child_parent = get_child_parent_relationships(
        relationship_file_path="data/static_cohort.parquet",
        filter_file_path="data/remapped_augmented.parquet",
    )

    # Get birth years for all children
    birth_years_df = get_birth_years()

    print("Creating education history...")
    create_education_history(child_parent, birth_years_df)

    print("Creating income history...")
    create_historical_data(
        "registers/ind/",
        "LOENMV_13",
        "income_history.parquet",
        child_parent,
        birth_years_df,
    )

    print("Creating socioeconomic status...")
    create_historical_data(
        "registers/akm/",
        "SOCIO13",
        "employment_history.parquet",
        child_parent,
        birth_years_df,
    )

    print("Creating family arrangement...")
    create_family_arrangement(child_parent, birth_years_df)

    print(f"All files have been saved to {OUTPUT_DIR}/")
