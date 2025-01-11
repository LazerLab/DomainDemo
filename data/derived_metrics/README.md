# Introduction

Here, we share the derived domain metrics across the whole time period.

# Files

We share six files, containing the following metrics that quantify different aspects of the domain sharing patterns.

| File name | N | Range | Description |
|-----------|------|-------|-------------|
| derived_state_kl.parquet | 129,127 | [0, ∞) | Localness of the domains, larger values indicate more local ones. |
| derived_age_kl.parquet | 129,127 | [0, ∞) | Age distribution deviation, larger values indicate that the domain shares are concentrated on a certain age groups. |
| derived_race_kl.parquet | 129,127 | [0, ∞) | Racial distribution deviation, larger values indicate that the domain shares are concentrated on a certain racial groups. |
| derived_party_leaning.parquet | 129,127 | [-1, 1] | Audience partisanship, negative values indicate more shares from Democratic users and vice versa. |
| derived_partyreg_leaning.parquet | 129,041 | [-1, 1] | Audience partisanship based on voter registration, negative values indicate more shares from Democratic users and vice versa. |
| derived_gender_leaning.parquet | 129,127 | [-1, 1] | Audience gender leaning, negative values indicate more shares from female users and vice versa. |

Each file contains two columns, a `domain` column and a metric column (names vary across files).

Note that `derived_party_leaning.parquet` and `derived_partyreg_leaning.parquet` both measure the audience partisanship.
The former is based on inferred partisanship of the voters whereas the latter is based on voter registration data.
Despite the differences, the two measures are highly correlated, with a Pearson correlation coefficient of 0.92.
For details, please refer to our paper.

# Usage

These files are in parquet format, and can be loaded using `pandas.read_parquet` for Python users:

```python
import pandas as pd

df = pd.read_parquet("derived_state_kl.parquet")
```

Users of other languages can use the corresponding tools to load the files.