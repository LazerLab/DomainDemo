# Introduction

This folder contains the code to generate derived metrics from the raw data.
We will use the sharing distribution for the whole time period, but the code can be applied to more granular time periods.

Before running the code, please download the `DomainDemo-univariate` data from the data repository and put them in the `data/raw` folder.
Specifically, make sure the data in `alltime` is present.

# Prerequisites

Note that we use [snakemake](https://snakemake.readthedocs.io/en/stable/) to run the workflow.
Please refer to the official website for instructions on how to install and use it.