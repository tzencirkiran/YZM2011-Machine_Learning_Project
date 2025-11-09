# DSA210-TopMovies
# Top Movies

## Description
This study looks at the 5,000 highest‑ranked movies on IMDb. We join their basic info with TMDB numbers for budget and revenue, fix missing or zero values, and create new measures like profit and ROI. We then explore trends over time, spot top‑earning directors, and check how factors such as budget, year, runtime and rating relate to money made. Finally, we train simple machine‑learning models: regressors to predict profit and rating, classifiers to label films by quality and popularity, and K‑means to group movies by their financial shape.

# Description Of Datasets
## Main Dataset (IMDB)
This is our main dataset containing information about the top 5000 movies in IMDB.
- **tconst:** Unique IMDB title ID
- **primaryTitle:** Original movie title
- **startYear:** Release year
- **rank:** Position in IMDB Top 5000 ranking
- **averageRating:** Average IMDB rating
- **numVotes:** Number of IMDb votes
- **runtimeMinutes:** Movie length (in minutes)
- **directors:** Director(s) name(s)
- **writers:** Writer(s) name(s)
- **genres:** Movie genres (e.g. Drama, Action)
## Supplementary Data from TMDB
- **tmdb_titles:** Title returned by the TMDB API
- **budget:** Production budget in USD
- **revenue:** Revenue in USD

## Tools and Technologies
- **Python:** Data Collection & Analysis
- **Jupiter Notebook:** Main program for coding, documentation and visual analysis
- **Pandas:** Data cleaning and manipulation
- **Matplotlib:** Basic data visualization
- **Seaborn:** Advanced and styled data visualizations
- **SciPy:** Statistical Hypothesis Testing
- **TMDB API:** To enrich the dataset with movie budgets and revenues

# Plan
## Data Collection
- Clean and merge datasets with Pandas
- Visualise distributions and correlations with Matplotlib/Seaborn
## Feature Engineering
- **profit:** Revenue - budget
- **roi:** Profit / budget
- **popularity:** Classification of popularity level 
- **good_or_avg:** Classification of rating
## Data Analysis
- I will clean the data with the help of the pandas library, analyse and visualize it with described python libraries(Matplotlib,Seaborn).
## Hypothesis Testing
- **Example Hypothesis:**
  - H₀: Budget of the movie has no effect on the rating.
  - Hₐ: Higher budgets make the movie get higher ratings.
## Expected Outcome
- Cleaned, merged dataset
- Jupyter notebook with EDA, tests, models
  
# Machine Learning
## Profit Prediction (Regression)**
- **Model**: RandomForestRegressor.
- **Predictors**: 'rank', 'startYear', 'averageRating', 'numVotes', 'runtimeMinutes', 'budget'.
- **Target**: 'profit'.
- **Evaluation Metrics**: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R2 Score are used.
## Average Rating Prediction (Regression)**
- **Model**: XGBRegressor.
- **Predictors**: 'startYear', 'numVotes', 'runtimeMinutes', 'budget', 'revenues'.
- **Target**: 'averageRating'.
- **Evaluation Metrics**: MAE, MSE, RMSE, and R2 Score.
## Good or Average Prediction (Binary Classification)**
- **Model**: LogisticRegression.
- **Predictors**: 'startYear', 'numVotes', 'runtimeMinutes', 'budget', 'revenues'.
- **Target**: 'good_or_avg'.
- **Evaluation Metrics**: Classification Report (precision, recall, f1-score, support, accuracy, macro avg, weighted avg).
## Popularity Level Classification (Multi-class Classification)**
- **Model**: RandomForestClassifier.
- **Predictors**: 'rank', 'startYear', 'runtimeMinutes', 'averageRating', 'budget', 'revenues'.
- **Target**: 'popularity'.
- **Evaluation Metrics**: Classification Report.
## Financial Profile Clustering (Unsupervised Learning)**
- **Method**: K-means Clustering.
- **Features for Clustering**: 'budget', 'revenues'.
- **Optimal Number of Clusters**: Determined using the silhouette score, with 2 identified as optimal.
- **Evaluation**: Silhouette Score is used to evaluate the clustering quality.
- **Visualization**: A scatter plot shows the clustered movies based on budget and revenue, with different colors representing different clusters.

# Future Extensions
- Express all financial values in constant 2025 dollar.
- Add marketing spend where data become available.
- Develop a classification model that labels planned films as successful or not.

# Conclusion
- This project provided a detailed analysis of IMDb’s Top 5000 movies by appending financial data and applying both statistical and machine learning methods. Studies revealed only weak to moderate correlations between features like budget, runtime, and ratings, indicating that high spending does not guarantee higher ratings. The machine learning models showed reasonable performance in predicting profit, rating, and popularity levels, while K means clustering effectively segmented movies based on financial profiles. Overall, this project indicates how data driven techniques can uncover unique patterns in the film industry and sets a foundation for future improvements with advanced models and additional data sources.
