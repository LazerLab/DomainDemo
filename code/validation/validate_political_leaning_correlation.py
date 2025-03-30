"""
This script validates the correlation between existing political bias labels and calculated political leaning scores.

It reads the existing political bias labels and calculated political leaning scores, merges them, and computes the Spearman correlation
between each existing label and each calculated leaning score metric. The results are saved to a CSV file.

Usage:
    python validate_political_leaning_correlation.py <existing_political_bias_labels_path> <political_leaning_score_path> <political_leaning_score_partyreg_path> <output_path>

Arguments:
    existing_political_bias_labels_path: Path to the CSV file containing existing political bias labels.
    political_leaning_score_path: Path to the csv.gz file containing calculated political leaning scores.
    political_leaning_score_partyreg_path: Path to the csv.gz file containing calculated political leaning scores for party registration.
    output_path: Path to save the output CSV file containing the correlation results.
"""

import pandas as pd
import sys
import scipy.stats

existing_political_bias_labels_path = sys.argv[1]
political_leaning_score_path = sys.argv[2]
political_leaning_score_partyreg_path = sys.argv[3]

output_path = sys.argv[-1]

existing_political_bias_labels_df = pd.read_csv(existing_political_bias_labels_path)

political_leaning_score_df = pd.read_csv(political_leaning_score_path)
political_leaning_score_partyreg_df = pd.read_csv(political_leaning_score_partyreg_path)
political_leaning_score_partyreg_df.rename(
    columns={
        "leaning_score": "leaning_score_reg",
    },
    inplace=True,
)

partisan_leaning_score_merged = existing_political_bias_labels_df.merge(
    political_leaning_score_df, on="domain"
).merge(political_leaning_score_partyreg_df, on="domain")

classification_cols = [
    "fb_score",
    "mturk_score",
    "allsides_score",
    "allsides_score_community",
    "mbfc_score",
    "media_score",
    "buntain_share_ideology_score",
]
corr_list = []
for col in classification_cols:
    for metric in [
        "leaning_score",
        "leaning_score_reg",
    ]:
        temp_df = partisan_leaning_score_merged[[metric, col]].dropna()
        rho, p = scipy.stats.spearmanr(temp_df[metric], temp_df[col])
        corr_list.append([col, metric, rho, p, len(temp_df)])
corr_df = pd.DataFrame(
    corr_list,
    columns=[
        "existing_label",
        "metric",
        "rho",
        "p",
        "n",
    ],
)

corr_df.to_csv(output_path, index=False)
