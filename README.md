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
│   └── raw/                   # Airbnb listings data (downloaded via script)
│       ├── copenhagen_listings_2025_03_train.csv
│       ├── copenhagen_listings_2025_09_test.csv
│       └── oslo_listings_2025_09_test.csv
├── scripts/
│   └── fetch_data.py          # Download data from Inside Airbnb
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
- Training: Copenhagen March 2025 (Inside Airbnb scrape)
- Temporal validation: Copenhagen September 2025 (6 months later, same city)
- Spatial validation: Oslo September 2025 (same time, different city)

## License

MIT
