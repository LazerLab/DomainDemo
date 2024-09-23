"""
This script loads a dataset from a Parquet file and prints the first few rows.

Usage:
    python load_data.py <input_file>

Arguments:
    input_file: str
        The path to the input Parquet file.

Example:
    python load_data.py data/raw/sample.parquet
"""

import pandas as pd
import sys

input_file = sys.argv[1]

df = pd.read_parquet(input_file)

print(df.head())
