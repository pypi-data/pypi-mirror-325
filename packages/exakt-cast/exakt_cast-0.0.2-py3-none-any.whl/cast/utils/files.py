import os
from pathlib import Path
import polars as pl


def list_files():
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "queries")
    files = os.listdir(lookup_dir)

    new_files = []
    for file in files:
        if file.endswith(".sql"):
            new_files.append(file)

    return new_files


def first_file():
    home = Path.home()
    lookup_dir = os.path.join(home, "Documents", "Cast", "queries")
    files = os.listdir(lookup_dir)
    for file in files:
        if file.endswith(".DS_Store"):
            continue
        else:
            return file


def load_file(file_name):
    home = Path.home()
    file_dir = os.path.join(home, "Documents", "Cast", "queries", file_name)
    with open(file_dir, "r") as f:
        text = f.read()
    return text


def save_file(file_name, text):
    home = Path.home()
    file_dir = os.path.join(home, "Documents", "Cast", "queries", file_name)
    with open(file_dir, "w") as f:
        f.write(text)


def delete_file(file):
    home = Path.home()
    file_dir = os.path.join(home, "Documents", "Cast", "queries", file)
    os.remove(file_dir)


def remove_incomplete_rows(df: pl.DataFrame, threshold: float = 0.54) -> pl.DataFrame:
    """
    Removes rows from a Polars DataFrame with more than the specified percentage of null values.

    Parameters:
        df (pl.DataFrame): The input Polars DataFrame.
        threshold (float): The fraction of null values allowed per row (default is 0.5).

    Returns:
        pl.DataFrame: A DataFrame with rows removed based on the null value threshold.
    """
    # Calculate the maximum allowed nulls per row
    null_limit = int(threshold * len(df.columns))

    schema = df.schema

    # Iterate through columns and apply NaN replacement for numeric types only
    filtered_df = (
        df.with_columns(
            [
                # Apply the transformation only for numeric columns
                pl.when(pl.col(col).is_nan()).then(None).otherwise(pl.col(col)).alias(col)
                if schema[col] in [pl.Float32, pl.Float64]
                else pl.col(col)
                for col in df.columns
            ]
        )
        .with_columns(sum([pl.col(col).is_null().cast(int) for col in df.columns]).alias("null_count"))
        .filter(pl.col("null_count") <= null_limit)
        .drop("null_count")
    )  # Remove the temporary null count column

    return filtered_df
