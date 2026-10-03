# Pattern Mining Agent

An Excel-based data analysis project designed to discover potentially meaningful structures in datasets, summarize supporting evidence, and suggest research hypotheses for further investigation.

The first version is intended to run in **Google Colab**. It uses Python's statistical and machine-learning libraries. CrewAI can be added later to coordinate analysis tasks and generate natural-language explanations.

> **Important:** Detected patterns and generated hypotheses are exploratory. Correlation, association, clustering, and anomaly scores do not by themselves establish causation or prove that a pattern is scientifically meaningful.

## Features

The planned Pattern Mining Agent investigates:

1. **Correlations** — Pearson and Spearman relationships between numeric variables.
2. **Associations** — frequent itemsets and association rules for categorical or discretized data.
3. **Trends** — changes over time or sequence, where a meaningful ordering variable exists.
4. **Clusters** — groups of similar observations using methods such as K-Means and DBSCAN.
5. **Anomalies** — observations that differ from the broader dataset, using methods such as Isolation Forest.
6. **Nonlinear relationships** — dependencies that may not be captured by simple linear correlation, including mutual information and nonlinear model comparisons.
7. **Feature interactions** — relationships where the association between two variables depends on another variable.

The agent should also profile the dataset, document data-quality issues, and produce an evidence-based report with limitations and follow-up questions.

## Current Status

This repository describes the project structure and development plan. Implement only the analyses that are present and tested in the current notebook or source code. Do not treat planned features as completed functionality.

## Technology Stack

- Python
- Google Colab
- Pandas and NumPy
- SciPy and Statsmodels
- Scikit-learn
- Matplotlib and Seaborn
- OpenPyXL for Excel files
- MLxtend for association-rule mining
- Optional: CrewAI and a supported language-model API

## Getting Started in Google Colab

### 1. Open the notebook

Open [Google Colab](https://colab.research.google.com/) and create a new notebook, or open the project's notebook if one has been added to this repository.

### 2. Install the core dependencies

Run this in a notebook cell:

```python
!pip -q install pandas numpy openpyxl scipy scikit-learn matplotlib seaborn mlxtend statsmodels
```

### 3. Upload an Excel dataset

Run:

```python
from google.colab import files
import pandas as pd

uploaded = files.upload()
file_name = next(iter(uploaded))
df = pd.read_excel(file_name)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
display(df.head())
```

For a workbook with multiple sheets, specify a sheet name or sheet index in `pd.read_excel()`.

### 4. Inspect data quality

```python
print("Shape:", df.shape)
print("Data types:")
print(df.dtypes)

print("\nMissing values:")
display(df.isna().sum().sort_values(ascending=False))

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumerical summary:")
display(df.describe(include="all").T)
```

### 5. Run the available analyses

Use the analysis functions included in the current notebook or `src/` modules. The agent should skip methods that are unsuitable for the supplied data and explain why. For example, trend analysis generally needs a time or sequence column, while association-rule mining requires suitable categorical or discretized features.

## Recommended Project Structure

```text
pattern-mining-agent/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── Pattern_Mining_Agent.ipynb
├── src/
│   ├── data_loader.py
│   ├── data_profiler.py
│   ├── correlation_miner.py
│   ├── association_miner.py
│   ├── trend_miner.py
│   ├── clustering_miner.py
│   ├── anomaly_detector.py
│   ├── nonlinear_miner.py
│   ├── interaction_miner.py
│   └── report_generator.py
├── tests/
│   └── test_basic_analysis.py
└── sample_data/
    └── README.md
```

This is a suggested structure. Create modules as the notebook becomes stable; a single notebook is sufficient for the earliest prototype.

## Expected Report

A completed run should aim to produce:

- Dataset profile and data-quality summary
- Correlation results and suitable statistical tests
- Association rules with support, confidence, and lift
- Trend summaries where time or sequence information is available
- Cluster assignments, cluster profiles, and evaluation metrics
- Anomaly flags with the detection method documented
- Nonlinear dependence results and validation notes
- Feature-interaction results with model assumptions and uncertainty
- Candidate hypotheses linked to specific evidence
- Limitations, alternative explanations, and suggested follow-up analyses
- Exportable result tables and a report (Markdown, HTML, or PDF)

## How Hypotheses Should Be Reported

For each candidate finding, include:

- **Observation:** what the data analysis found.
- **Evidence:** relevant statistics, sample size, uncertainty, and validation results.
- **Potential hypothesis:** a cautious explanation or relationship to investigate.
- **Alternative explanations:** possible confounders, measurement issues, or selection effects.
- **Follow-up:** a test or analysis that could help assess the hypothesis.
- **Limitations:** what the current data cannot establish.

Do not label a hypothesis as proven based only on exploratory results. Consider multiple-testing effects when screening many relationships, and validate promising findings on independent data when possible.

## Data Handling and Privacy

- Do not upload confidential, personally identifiable, or restricted institutional data to a public repository.
- Use synthetic, public, or otherwise authorized sample data.
- Never commit API keys, passwords, tokens, or private configuration files.
- Do not automatically remove missing values, duplicates, or outliers without documenting the decision.
- Preserve the original uploaded dataset and work on an analysis copy.
- Review notebook outputs before committing; notebooks can contain data previews, file paths, or secrets.

## Optional CrewAI Integration

CrewAI may be added after the core analysis functions work reliably. A simple architecture is one main Pattern Mining Agent coordinating deterministic Python functions for profiling and analysis, then asking a language model to explain the verified results.

Recommended separation of responsibilities:

- **Python analysis functions:** calculate statistics, rules, clusters, anomalies, and metrics.
- **Pattern Mining Agent:** choose relevant analyses and organize findings.
- **Evidence review:** check that each statement is supported by computed results and includes limitations.
- **Report generation:** create a structured, readable report.

If a language-model API is used, store credentials in Colab Secrets or environment variables. Never hard-code keys in notebooks or commit them to GitHub.

## Testing Checklist

Test with different datasets before relying on the results:

- Numeric-only data
- Categorical-only data
- Mixed numeric and categorical data
- Time-series or sequence data
- Missing values and duplicate rows
- Constant columns and highly correlated features
- Small datasets
- High-cardinality categorical columns
- Larger datasets that may require runtime or memory safeguards

Check both whether code runs and whether the resulting interpretations are reasonable.

## Publishing to GitHub

1. Create a repository named `pattern-mining-agent`.
2. Add this `README.md`.
3. Download the notebook from Colab using **File → Download → Download .ipynb**.
4. Upload the notebook and project files to the repository.
5. Add a `requirements.txt` containing the dependencies actually used.
6. Add a `.gitignore` file to exclude local secrets, temporary outputs, and private datasets.
7. Review notebook outputs and repository visibility before committing.

Useful references:

- [Google Colab](https://colab.research.google.com/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn documentation](https://scikit-learn.org/stable/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)
- [MLxtend documentation](https://rasbt.github.io/mlxtend/)
- [CrewAI documentation](https://docs.crewai.com/)
- [GitHub: Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

## License

No license has been selected yet. Before making the repository public, choose a license appropriate for how you want others to use, modify, and distribute the project.
