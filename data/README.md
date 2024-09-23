This is the folder for storing raw & derived datasets. 
However, do not commit large datasets to the git repository. 

You can add patterns such as `*.csv` and `*.tsv` to `.gitignore` to ignore certain types of data files.

Follow one of the following practices:

1. If the raw data is small, consider committing it to the repository. You can still store derived datasets locally and ignore them with `.gitignore`.
1. Large and sensitive files should stay on the remote servers.
1. If the dataset has a fixed location (URL), integrate the script to download the dataset into the workflow. Git-ignore all downloaded and derived datasets. 

Finally, whenever possible, make sure that the raw data files are **read-only**.
You can use the structure suggested here: https://github.com/drivendata/cookiecutter-data-science#the-resulting-directory-structure 

```
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
```

Update this document to store detailed documentation (data dictionary) on the datasets. Document at least the following (ideally, create a [datasheet](https://arxiv.org/abs/1803.09010)):

1. _When_ was the data obtained?
2. _From whom_ or _where_ did you get the data?
3. What does each column mean? What is the _data format_ of each column? Loading a column with a wrong assumption about its data format can cost your project!
4. What are the other relevant information, restrictions, and limitations about the dataset? How was the data collected? What kinds of biases does it contain? What should not be done with the dataset (e.g., identification of individuals)?
