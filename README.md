# Introduction

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15151613.svg)](https://doi.org/10.5281/zenodo.15151613)

This repository contains the code and part of the data for the dataset [DomainDemo: a dataset of domain-sharing activities among different demographic groups on Twitter](https://arxiv.org/abs/2501.09035).

# Directory Structure

- [/code](/code): for example scripts to load the data and workflow to generate derived metrics
- [/data](/data): for data

# Data access

DomainDemo contains the following versions:
- `DomainDemo-multivariate`: multivariate version of the dataset
- `DomainDemo-univariate`: univariate version of the dataset
- `derived_metrics`: derived metrics for the domains

All these versions are hosted on [Zenodo](https://zenodo.org/record/15151613).
Due to the sensitive nature of `DomainDemo-multivariate` and `DomainDemo-univariate`, researchers interested in accessing them need to apply for access.
Detailed instructions are available on the Zenodo page.

The `derived_metrics` is available for public access.
These metrics quantify different aspects, such as localness and audience partisanship, for over 129,000 domains.
For details, please refer to the [derived metrics](/data/derived_metrics/README.md) page.

We also provide an interactive app to allow everyone to explore the data.
The app is hosted on [domaindemoexplorer.streamlit.app](https://domaindemoexplorer.streamlit.app/).

# Citation

If you use this dataset in your research, please cite the following paper:

```bibtex
@misc{yang2025domaindemo,
	title={DomainDemo: a dataset of domain-sharing activities among different demographic groups on Twitter},
	author={Kai-Cheng Yang and Pranav Goel and Alexi Quintana-Mathé and Luke Horgan and Stefan D. McCabe and Nir Grinberg and Kenneth Joseph and David Lazer},
	year={2025},
	eprint={2501.09035},
	archivePrefix={arXiv},
	primaryClass={cs.SI},
	url={https://arxiv.org/abs/2501.09035},
	journal={arxiv:2501.09035}
}
```
