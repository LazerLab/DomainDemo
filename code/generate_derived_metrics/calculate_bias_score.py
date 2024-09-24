"""
This script calculates the bias score for different domains based on binary demographic data.

Usage:
    python calculate_bias_score.py <univariate_path> <univariate_all_domains_path> <demo> <left_category> <right_category> <output_path>

Arguments:
    univariate_path: str
        The path to the input Parquet file containing univariate data. This file contain the user distribution of each domain across different categories in the demographic dimensions.
    univariate_all_domains_path: str
        The path to the input Parquet file containing univariate data for all domains. This file contain the user distribution of all domains across different categories in the demographic dimensions and serves as the baseline.
    demo: str
        The demographic category to be used for the calculation.
    left_category: str
        The left category of the binary demographic dimension.
    right_category: str
        The right category of the binary demographic dimension.
    output_path: str
        The path to the output Parquet file where the bias score results will be saved.
"""

import pandas as pd
import sys

univariate_path = sys.argv[1]
univariate_all_domains_path = sys.argv[2]
demo = sys.argv[3]
left_category = sys.argv[4]
right_category = sys.argv[5]
output_path = sys.argv[-1]

univariate_df = pd.read_parquet(univariate_path)
univariate_all_domains_df = pd.read_parquet(univariate_all_domains_path)
univariate_all_domains_df.rename(columns={"users": "demo_total_users"}, inplace=True)

raw_count_binary_df = univariate_df.merge(univariate_all_domains_df, on=demo)

raw_count_binary_df[f"users_portion"] = (
    raw_count_binary_df["users"] / raw_count_binary_df["demo_total_users"]
)

portion_df = raw_count_binary_df.pivot_table(
    index="domain", columns=demo, values="users_portion", fill_value=0
).reset_index()

portion_df[f"bias_score"] = (portion_df[right_category] - portion_df[left_category]) / (
    portion_df[right_category] + portion_df[left_category]
)

portion_df.dropna(inplace=True)

portion_df[["domain", "bias_score"]].to_parquet(output_path, index=False)
