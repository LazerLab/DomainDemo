"""
This script merges localness scores with existing localness labels.

It reads the existing localness labels and localness scores, merges them based on the domain,
filters out inconsistent classifications, and saves the merged data to a CSV file.

Usage:
    python merge_localness_score_with_labels.py <existing_localness_labels_path> <localness_score_path> <output_path>

Arguments:
    existing_localness_labels_path: Path to the CSV file containing existing localness labels.
    localness_score_path: Path to the parquet file containing localness scores.
    output_path: Path to save the output CSV file containing the merged data.
"""

import pandas as pd
import sys

existing_localness_labels_path = sys.argv[1]
localness_score_path = sys.argv[2]

output_path = sys.argv[-1]

local_classification_df = pd.read_csv(existing_localness_labels_path)
localness_score_df = pd.read_csv(localness_score_path)

local_classification_df = local_classification_df.query(
    f"classification != 'INCONSISTENT'"
)

localness_score_merged = localness_score_df.merge(local_classification_df, on="domain")
print(
    f"{len(localness_score_merged)} / {len(localness_score_df)} = {len(localness_score_merged) / len(localness_score_df) * 100:.2f}% domains matched"
)

localness_score_merged.to_csv(output_path, index=False)
