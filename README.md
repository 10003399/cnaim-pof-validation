# CNAIM Probability of Failure Validation

**Reliability Analysis of Electrical Network Assets**

---

## Project Background

Electric power distribution networks rely on risk models to ensure reliable electricity delivery while optimizing maintenance investments. One commonly used framework is **CNAIM (Common Network Asset Indices Methodology)**, which estimates the **Probability of Failure (PoF)** and associated asset risk.

This project investigates how well CNAIM predictions align with observed failure behaviour by analysing historical asset and failure data using statistical reliability methods.

---

## Project Objective

The primary objective is to validate and calibrate CNAIM failure probabilities by comparing:

* Model-predicted failure risk (CNAIM PoF)
* Empirically observed failure statistics
* Age-dependent reliability behaviour

The goal is to determine whether the model accurately represents real operational conditions and to identify opportunities for improved predictive maintenance.

---

## Methodology

### 1. Data Preparation

* Asset inventory and failure history were imported and validated.
* Data quality checks ensured unique asset identifiers and consistent time information.
* An **asset-years exposure dataset** was constructed, where each row represents one asset operating during one year of service.

This exposure modelling step enables statistically correct estimation of failure rates.

---

### 2. Observed Failure Analysis

Observed failure intensity was calculated as:

Observed Failure Rate = Total Failures / Total Exposure Time

Failure behaviour was aggregated by asset category to enable comparison with CNAIM PoF values.

---

### 3. Reliability Modelling

Two complementary reliability approaches were applied:

#### Weibull Reliability Analysis

A Weibull distribution was fitted to failure ages to characterize degradation behaviour.

Results indicated:

* **β ≈ 5.9** → strongly age-dependent failures
* Failure risk increases rapidly with asset ageing
* Evidence of wear-out dominated failure mechanisms

This supports the use of predictive or condition-based maintenance strategies.

---

#### Kaplan–Meier Survival Analysis

Survival analysis was used to correctly incorporate assets that have **not yet failed** (censored observations).

Outputs include:

* Survival probability over asset lifetime
* Median survival estimation
* Realistic reliability representation of the asset population

---

### 4. CNAIM Model Calibration

Empirical failure rates were compared with CNAIM PoF predictions.

Key findings:

* Cable assets showed higher observed failure rates than predicted by CNAIM.
* A calibration factor (~2.25) suggests CNAIM underestimates cable failure risk under local conditions.
* Other asset classes contained insufficient failure observations for statistically reliable calibration.

A global calibration factor was derived to adjust PoF estimates toward observed network behaviour.

---

## Key Outcomes

* Construction of a reproducible reliability analysis workflow
* Validation of model assumptions against operational data
* Identification of ageing-driven failure mechanisms
* Quantitative calibration approach for risk models
* Foundation for predictive maintenance prioritization

---

## Repository Structure

```
src/            Analysis modules and reusable functions
notebook/       Exploratory analysis and modelling workflow
data/
  raw/          Local input data (not version controlled)
  processed/    Generated analysis datasets
reports/        Figures and analytical outputs
tests/          Validation tests
```

---

## Technologies Used

* Python
* pandas
* NumPy
* SciPy
* lifelines (survival analysis)
* matplotlib
* JupyterLab
* Git / GitHub

---

## Engineering Relevance

The workflow mirrors real asset performance analysis performed within power system operators and infrastructure companies. The methods support:

* Risk-based maintenance planning
* Asset life estimation
* Investment prioritization
* Reliability-centred decision making

---

## Future Work

* Asset-level risk ranking
* Environmental and loading factor modelling
* Adva


A risk ranking framework was implemented combining calibrated Probability of Failure with estimated consequence factors. The resulting risk score enables prioritization of maintenance actions and supports risk-based asset management decisions.