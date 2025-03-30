#!/usr/bin/env Rscript

# This script loads a dataset from a CSV.gz file and prints the first few rows.
#
# Usage:
#     Rscript load_data.R <input_file>
#
# Arguments:
#     input_file: character
#         The path to the input CSV.gz file.
#
# Example:
#     Rscript load_data.R data/raw/sample.csv.gz

# Load required package
if (!require(readr)) {
  install.packages("readr")
  library(readr)
}

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1) {
  stop("Please provide the input file path as an argument")
}

input_file <- args[1]

# Read the data
df <- read_csv(input_file)

# Print the first few rows
print(head(df))