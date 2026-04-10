# YZM2011 — Course Project: IMDb Top 5000 Movies

**Course:** YZM2011 — Introduction to Machine Learning  
**Instructor:** Ekrem Çetinkaya  
**Dataset:** [IMDb Top 5000 Movies — Kaggle](https://www.kaggle.com/datasets/tiagoadrianunes/imdb-top-5000-movies/data) + TMDB API

---

## Problem Description

What factors drive the financial success and audience reception of movies?

We combine IMDb ranking data for the top 5,000 movies with production budgets and box-office revenues fetched from the TMDB API. The goal is to understand which features (budget, runtime, genre, release year, vote count) best predict a film's financial outcome and audience rating — and to build progressively more sophisticated models across three deliverables.

**Research questions:**
1. How are ratings and financial metrics distributed across the dataset?
2. Which genres and directors dominate in terms of revenue and rating?
3. Are budget, runtime, and release year correlated with IMDb rating or profit?
4. Can we predict movie profit from observable pre-release features?
5. Can we classify a movie as "good" or "average" based on its attributes?

---

## Dataset

| Source | Content |
|--------|---------|
| `results_with_crew.csv` | IMDb Top 5000: title, year, rank, rating, votes, runtime, genres, directors, writers |
| `budget_revenue.csv` | TMDB API: production budget and box-office revenue per film |
| `diff_fix.csv` | Manual corrections for titles that mismatched between IMDb and TMDB |

**Engineered features:**
- `profit`: revenue − budget
- `roi`: profit / budget
- `good_or_avg`: binary label — 1 if rating ≥ 7.5, else 0
- `popularity`: 3-class label based on vote-count percentiles (0=low, 1=moderate, 2=high)

---

## Project Structure

This repository covers three deliverables for the same dataset:

| # | Notebook | Deliverable | Status |
|---|----------|-------------|--------|
| P1 | `p1_eda.ipynb` | Problem formulation, data cleaning, EDA, hypothesis testing | Ready for submission |
| P2 | `p2_regression.ipynb` | Regression — predicting movie profit | Draft / planned for Week 10 |
| P3 | Classification notebook | Predicting movie quality and popularity | Planned for Week 15 |

**How they connect:** P1 cleans and explores the data and defines the feature space. P2 will use those features for regression modelling (predicting `profit`). P3 will use the same cleaned dataset for classification modelling (`good_or_avg` and `popularity` labels defined in P1).

`top_movies.ipynb` is an earlier exploratory notebook kept for reference; `p1_eda.ipynb` is the submission notebook for P1.

---

## Running the Project

**P1 EDA:**
```bash
jupyter notebook p1_eda.ipynb
```

**Re-fetch TMDB financial data** (requires API key in `.env`):
```bash
python tmdb_api.py
python diff.py
```

**Setup:**
```bash
cp .env.example .env
# Fill in your TMDB_API_KEY in .env
pip install pandas numpy matplotlib seaborn scipy scikit-learn python-dotenv tmdbsimple
```

---

## Dependencies

`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`, `python-dotenv`, `tmdbsimple`
