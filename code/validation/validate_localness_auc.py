"""
This script validates the localness AUC (Area Under the Curve) for given localness scores.

It reads the merged localness labels and localness scores from a CSV file, calculates the AUC for different metrics, and saves the results to an output CSV file.

Usage:
    python validate_localness_auc.py <localness_score_merged_path> <output_path>

Arguments:
    localness_score_merged_path: Path to the CSV file containing merged localness labels and scores.
    output_path: Path to save the output CSV file containing the AUC result.
"""

import pandas as pd
import sys
import sklearn.metrics

localness_score_merged_path = sys.argv[1]

output_path = sys.argv[-1]

localness_score_merged_df = pd.read_csv(localness_score_merged_path)

result_list = []
auc = sklearn.metrics.roc_auc_score(
    localness_score_merged_df.classification == "local",
    localness_score_merged_df.kl_divergence,
)
result_list.append(auc)

result_df = pd.DataFrame(result_list, columns=["auc"])
result_df.to_csv(output_path, index=False)
