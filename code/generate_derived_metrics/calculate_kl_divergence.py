"""
This script calculates the Kullback-Leibler (KL) divergence for different domains based on demographic data.

Usage:
    python calculate_kl_divergence.py <univariate_distribution_path> <univariate_baseline_path> <demo> <output_path>

Arguments:
    univariate_distribution_path: str
        The path to the input csv.gz file containing univariate data. This file contain the user distribution of each domain across different categories in the demographic dimensions.
    univariate_baseline_path: str
        The path to the input csv.gz file containing univariate data for all domains. This file contain the user distribution of all domains across different categories in the demographic dimensions and serves as the baseline.
    demo: str
        The demographic category to be used for the calculation.
    output_path: str
        The path to the output csv.gz file where the KL divergence results will be saved.
"""

import sys
import pandas as pd
import numpy as np

univariate_distribution_path = sys.argv[1]
univariate_baseline_path = sys.argv[2]
demo = sys.argv[3]
output_path = sys.argv[-1]

univariate_distribution_df = pd.read_csv(univariate_distribution_path)
print(f"Len of univariate distribution df: {len(univariate_distribution_df)}")

univariate_baseline_df = pd.read_csv(univariate_baseline_path)
univariate_baseline_df.rename(columns={"users": "demo_total_users"}, inplace=True)
print(f"Len of univariate baseline df: {len(univariate_baseline_df)}")

df = univariate_distribution_df.merge(univariate_baseline_df, on=demo)

df["total_users"] = univariate_baseline_df["demo_total_users"].sum()
domain_total_col_count = (
    univariate_distribution_df.groupby("domain")["users"]
    .sum()
    .to_frame("domain_total_users")
    .reset_index()
)
df = df.merge(domain_total_col_count, on="domain")
df["f_c"] = df["demo_total_users"] / df["total_users"]
df["f_dc"] = df["users"] / df["domain_total_users"]
df["kl_divergence"] = df["f_dc"] * np.log2(df["f_dc"] / df["f_c"])

kl_divergence = df.groupby("domain")["kl_divergence"].sum().to_frame().reset_index()

kl_divergence.dropna(inplace=True)

kl_divergence.to_csv(output_path, index=False)
