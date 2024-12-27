# Introduction

This folder stores the released data files.

# Structure

## `monthly`

Data files split by month.

- `multivariate`: The DomainDemo-multivariate tables
- `univariate`: The DomainDemo-univariate tables, with subfolders for each universe (e.g., age, gender, etc.)
- `univariate_all_domains`: The aggregated statistics across all domains for each universe (e.g., age, gender, etc.)

## `alltime`

Data files aggregated across all months.
The main purpose of these files is to generate the derived metrics across the whole time period.
Therefore, only the univariate data tables are included.

- `univariate`: The DomainDemo-univariate tables aggregated across all months, with subfolders for each universe (e.g., age, gender, etc.)
- `univariate_all_domains`: The aggregated statistics across all domains for each universe (e.g., age, gender, etc.)

## `derived_metrics`

The derived metrics across the whole time period.