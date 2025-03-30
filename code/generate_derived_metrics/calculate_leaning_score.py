"""
This script calculates the leaning scores for different domains based on binary demographic data.

Usage:
    python calculate_leaning_score.py <univariate_distribution_path> <univariate_baseline_path> <demo> <left_category> <right_category> <output_path>

Arguments:
    univariate_distribution_path: str
        The path to the input csv.gz file containing univariate data. This file contain the user distribution of each domain across different categories in the demographic dimensions.
    univariate_baseline_path: str
        The path to the input csv.gz file containing univariate data for all domains. This file contain the user distribution of all domains across different categories in the demographic dimensions and serves as the baseline.
    demo: str
        The demographic category to be used for the calculation.
    left_category: str
        The left category of the binary demographic dimension.
    right_category: str
        The right category of the binary demographic dimension.
    output_path: str
        The path to the output csv.gz file where the leaning score results will be saved.
"""

import pandas as pd
import sys

univariate_distribution_path = sys.argv[1]
univariate_baseline_path = sys.argv[2]
demo = sys.argv[3]
left_category = sys.argv[4]
right_category = sys.argv[5]
output_path = sys.argv[-1]

univariate_distribution_df = pd.read_csv(univariate_distribution_path)
univariate_baseline_df = pd.read_csv(univariate_baseline_path)
univariate_baseline_df.rename(columns={"users": "demo_total_users"}, inplace=True)

raw_count_binary_df = univariate_distribution_df.merge(univariate_baseline_df, on=demo)

raw_count_binary_df[f"users_portion"] = (
    raw_count_binary_df["users"] / raw_count_binary_df["demo_total_users"]
)

portion_df = raw_count_binary_df.pivot_table(
    index="domain", columns=demo, values="users_portion", fill_value=0
).reset_index()

portion_df[f"leaning_score"] = (
    portion_df[right_category] - portion_df[left_category]
) / (portion_df[right_category] + portion_df[left_category])

portion_df.dropna(inplace=True)

portion_df[["domain", "leaning_score"]].to_csv(output_path, index=False)
