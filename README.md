# Introduction

This repository contains the code and part of the data for the dataset [DomainDemo: a dataset of domain-sharing activities among different demographic groups on Twitter](https://arxiv.org/abs/2501.09035).

# Directory Structure

- [/code](/code): for example scripts to load the data and workflow to generate derived metrics
- [/data](/data): for data

# Data

Details on how to access `DomainDemo-multivariate` and `DomainDemo-univariate` will be provided soon.

At the moment, we make the derived domain metrics available.
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
