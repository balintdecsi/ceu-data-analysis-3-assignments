# CEU Data Analysis 3 Assignments

Coursework for **Data Analysis 3: Prediction and Machine Learning** at Central European University (MS in Business Analytics).

## Project Structure

```
├── assignments/
│   └── assignment-1/          # Airbnb pricing prediction model
│       └── assignment-1.ipynb
├── course_material/           # Class notebooks for reference
│   ├── class-13-framework-for-prediction/
│   ├── class-14-model-building-for-prediction/
│   ├── class-15-regression-trees/
│   └── class-16-random-forest-and-boosting/
├── data/
│   └── raw/                   # Airbnb listings data
│       ├── copenhagen_listings.csv
│       └── oslo_listings.csv
├── pyproject.toml             # Project dependencies (uv)
└── requirements.txt           # Pinned dependencies
```

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ceu-data-analysis-3-assignments.git
   cd ceu-data-analysis-3-assignments
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

   Or using `requirements.txt` with pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter notebooks:**
   ```bash
   uv run jupyter notebook
   ```

## Assignments

### Assignment 1: Airbnb Pricing Prediction

**Objective:** Build and compare 5 predictive models for Airbnb listing prices.

**Models implemented:**
- OLS (Ordinary Least Squares)
- LASSO (L1 regularization)
- Ridge (L2 regularization)
- Random Forest
- Gradient Boosting

**Data:**
- Training: Copenhagen Airbnb listings (~9,000 observations)
- Temporal validation: Copenhagen holdout (30%)
- Spatial validation: Oslo listings (~8,000 observations)

**Key findings:**
- Gradient Boosting achieves best temporal validation (RMSE: 514)
- LASSO achieves best spatial validation (RMSE: 622)
- Top predictors: accommodates, beds, bathrooms, room type

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | ≥3.0.0 | Data manipulation |
| numpy | ≥2.4.2 | Numerical computing |
| scikit-learn | ≥1.8.0 | ML models (LASSO, Ridge, RF, GB) |
| statsmodels | ≥0.14.6 | OLS regression |
| matplotlib | ≥3.10.8 | Visualization |
| seaborn | ≥0.13.2 | Statistical plots |

## License

MIT
