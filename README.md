# CNAIM Probability of Failure Validation

## Project Overview

This project evaluates how well the **CNAIM (Common Network Asset Indices Methodology)** model predicts failures in electrical network assets. The objective is to compare CNAIM’s calculated **Probability of Failure (PoF)** with observed historical failure data and assess whether the model accurately represents real network behavior.

## Purpose

Electric grid operators rely on risk models to prioritize maintenance and investments. By validating CNAIM predictions against empirical data, this project investigates:

* Whether CNAIM overestimates or underestimates failure risk
* Differences between modeled and observed asset performance
* Potential improvements for predictive and condition-based maintenance strategies

## Methodology

1. **Data Preparation**

   * Load asset information and failure history
   * Validate data quality and structure
   * Construct an *asset-years* exposure dataset

2. **Failure Analysis**

   * Calculate observed failure rates per asset type
   * Aggregate exposure time and failure counts
   * Compare empirical failure probability with CNAIM PoF

3. **Model Evaluation**

   * Visual comparison of modeled vs observed risk
   * Quantification of model error
   * Identification of systematic deviations

## Repository Structure

```
src/            Core analysis modules
notebooks/      Exploratory analysis and validation workflow
data/
  raw/          Local input data (not tracked)
  processed/    Generated analysis datasets
tests/          Validation tests
reports/        Figures and analysis summaries
```

## Key Output

* Asset-years exposure dataset
* Observed failure rate estimates
* CNAIM model validation results
* Visual calibration comparison

## Technologies

* Python
* pandas
* matplotlib
* JupyterLab

## Status

Phase 1 completed: data validation, exposure modeling, and initial CNAIM comparison.
