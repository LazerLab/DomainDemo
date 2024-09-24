"""
This script calculates the Kullback-Leibler (KL) divergence for different domains based on demographic data.

Usage:
    python calculate_kl_divergence.py <univariate_path> <univariate_all_domains_path> <demo> <output_path>

Arguments:
    univariate_path: str
        The path to the input Parquet file containing univariate data. This file contain the user distribution of each domain across different categories in the demographic dimensions.
    univariate_all_domains_path: str
        The path to the input Parquet file containing univariate data for all domains. This file contain the user distribution of all domains across different categories in the demographic dimensions and serves as the baseline.
    demo: str
        The demographic category to be used for the calculation.
    output_path: str
        The path to the output Parquet file where the KL divergence results will be saved.
"""

import sys
import pandas as pd
import numpy as np

univariate_path = sys.argv[1]
univariate_all_domains_path = sys.argv[2]
demo = sys.argv[3]
output_path = sys.argv[-1]

univariate_df = pd.read_parquet(univariate_path)
print(f"Len of univariate df: {len(univariate_df)}")

univariate_all_domains_df = pd.read_parquet(univariate_all_domains_path)
univariate_all_domains_df.rename(columns={"users": "demo_total_users"}, inplace=True)
print(f"Len of univariate all domains df: {len(univariate_all_domains_df)}")

df = univariate_df.merge(univariate_all_domains_df, on=demo)

df[f"total_users"] = univariate_all_domains_df[f"demo_total_users"].sum()
domain_total_col_count = (
    univariate_df.groupby("domain")["users"]
    .sum()
    .to_frame("domain_total_users")
    .reset_index()
)
df = df.merge(domain_total_col_count, on="domain")
df[f"f_c"] = df[f"demo_total_users"] / df[f"total_users"]
df[f"f_dc"] = df["users"] / df[f"domain_total_users"]
df[f"kl_divergence"] = df[f"f_dc"] * np.log2(df[f"f_dc"] / df[f"f_c"])

kl_divergence = df.groupby("domain")[f"kl_divergence"].sum().to_frame().reset_index()

kl_divergence.dropna(inplace=True)

kl_divergence.to_parquet(output_path, index=False)
