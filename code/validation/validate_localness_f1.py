"""
This script validates the localness F1 score for given localness scores.

It reads the merged localness labels and localness scores from a CSV file, calculates the F1 score for different metrics at various thresholds, and saves the results to an output CSV file.

Usage:
    python validate_localness_f1.py <localness_score_merged_path> <output_path>

Arguments:
    localness_score_merged_path: Path to the CSV file containing merged localness labels and scores.
    output_path: Path to save the output CSV file containing the F1 score results.
"""

import pandas as pd
import numpy as np
import sys
import sklearn.metrics

localness_score_merged_path = sys.argv[1]

output_path = sys.argv[-1]

localness_score_merged_df = pd.read_csv(localness_score_merged_path)


f1_list_kl = []
max_kl_divergence = localness_score_merged_df["kl_divergence"].max()
for threshold in np.linspace(0, max_kl_divergence, 1000):
    f1 = sklearn.metrics.f1_score(
        localness_score_merged_df["classification"] == "local",
        localness_score_merged_df["kl_divergence"] > threshold,
    )
    f1_list_kl.append([threshold, f1])

f1_list_kl_df = pd.DataFrame(f1_list_kl, columns=["threshold", "f1"])
f1_list_kl_df.to_csv(output_path, index=False)
