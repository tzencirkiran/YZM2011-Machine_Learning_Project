import os
import pandas as pd
import numpy as np
import tmdbsimple as tmdb
from dotenv import load_dotenv

# Load API key from .env so it is never committed to the repository
load_dotenv()
tmdb.API_KEY = os.getenv("TMDB_API_KEY")

# To store which titles are mismatching between Kaggle dataset and TMDB API
diff = pd.DataFrame({"imdb_title": [], "tmdb_title": []})

# Read our Kaggle dataset
imdb_data = pd.read_csv("results_with_crew.csv")

# Store movie titles as a list for API calls
movie_titles = list(imdb_data["primaryTitle"])

# Instantiate a search object
search = tmdb.Search()

# Empty lists for new columns
imdb_titles = []
tmdb_titles = []
budgets = []
revenues = []
error_titles = []

for title in movie_titles:
    search.movie(query=title)

    # No results at all — record as error and skip
    if not search.results:
        print(f"No results found for: {title}")
        error_titles.append(title)
        imdb_titles.append(title)
        tmdb_titles.append(None)
        budgets.append(None)
        revenues.append(None)
        continue

    # Try to find an exact match (case-insensitive); fall back to first result
    matched = None
    for r in search.results:
        if r["title"].lower() == title.lower():
            matched = r
            break
    if matched is None:
        matched = search.results[0]

    # Fetch full movie details using the matched movie's TMDB ID
    movie = tmdb.Movies(matched["id"])
    info = movie.info()

    imdb_titles.append(title)
    tmdb_titles.append(info.get("title"))
    budgets.append(info.get("budget"))
    revenues.append(info.get("revenue"))

    # Log whether the title matched exactly or differed
    if movie.title == title:
        print(True)
    else:
        print(f"{title}  →  {movie.title}")
        diff.loc[len(diff)] = [title, movie.title]

    print(movie.budget)
    print(movie.revenue)
    print()

# Summary
print(diff)
print(f"\nError Titles:\n{error_titles}\n")

# Save results — index=False avoids an unnamed index column in the CSV
budget_revenue = pd.DataFrame({
    "imdb_title":  imdb_titles,
    "tmdb_titles": tmdb_titles,
    "budget":      budgets,
    "revenue":     revenues,
})
print(budget_revenue)
budget_revenue.to_csv("budget_revenue.csv", index=False)
diff.to_csv("diff.csv", index=False)
