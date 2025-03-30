# Code

This folder stores the scripts for data processing and analysis.

# Structure

- [example_code](./example_code): example code for the project
- [generate_derived_metrics](./generate_derived_metrics): scripts for generating the derived metrics
- [validation](./validation): scripts for validating the derived metrics

# Dependencies

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install the dependencies and manage the environment.

If you have uv installed, you can install the dependencies by running:

```bash
uv sync
```

You can run the scripts using uv by running:

```bash
uv run <script_name>.py
```

If you want to use other package managers, you can use the `requirements.txt` file at the root of the repository to install the dependencies.