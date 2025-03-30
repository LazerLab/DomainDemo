"""
This script loads a dataset from a CSV.gz file and prints the first few rows.

Usage:
    python load_data.py <input_file>

Arguments:
    input_file: str
        The path to the input CSV.gz file.

Example:
    python load_data.py data/raw/sample.csv.gz
"""

import pandas as pd
import sys

input_file = sys.argv[1]

df = pd.read_csv(input_file)

print(df.head())
