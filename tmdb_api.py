import pandas as pd
import numpy as np
import tmdbsimple as tmdb

# API KEY for to pull data from TMDB
tmdb.API_KEY = "260f7d68fecb569fc11ce48c80471254"

# To store which titles are mismatching from Kaggle dataset and tmbd api
diff = pd.DataFrame({"imdb_title" : [], "tmdb_title" : []})

# Read our Kaggle dataset as a dataframe
imdb_data = pd.read_csv("topMovies/results_with_crew.csv")

# Store our movies' titles as a list for API calls
movie_titles = imdb_data["primaryTitle"]
movie_titles = list(movie_titles)

# Instantiate a search object for movie titles that we are gonna search in API
search = tmdb.Search()

# Empty lists for newer columns
imdb_titles = []
tmdb_titles = []
budgets = []
revenues = []
# Some titles may fail to gather data from the API
error_titles = []

# for each title we have in imdb_data
for title in movie_titles:
    # response stores a dictionary for results of search
    response = search.movie(query=title)
    
    # Try to find an exact match (case-insensitive) in the search results
    matched = None
    if search.results:
        for r in search.results:
            if r['title'].lower() == title.lower():
                matched = r
                break
        else:
            try:
                matched = search.results[0]  # if no exact match, fallback to first result
            except:
                print(f"No results found for {title}")
                error_titles.append(title)
                imdb_titles.append(title)
                tmdb_titles.append(None)
                budgets.append(None)
                revenues.append(None)
                continue

        # Request movie info from tmdb api according to matched's id
        movie = tmdb.Movies(matched['id'])
        info = movie.info()
        imdb_titles.append(title)
        tmdb_titles.append(info.get('title'))
        budgets.append(info.get('budget'))
        revenues.append(info.get('revenue'))
    else:
        imdb_titles.append(title)
        tmdb_titles.append(None)
        budgets.append(None)
        revenues.append(None)

    # if imdb_data and tmdb's titles are equal no problem, prints True
    if movie.title == title:
        print(movie.title == title)
    # if they are not then prints both titles and store this values in diff(df)
    else:
        print(f"{title}, {movie.title}")
        diff.loc[len(diff)] = [title, movie.title]

    # Prints budget, revenue and then one empty line
    print(movie.budget)
    print(movie.revenue)
    print()

# Prints df which holds mismatching values for titles
print(diff)
# Prints, in which titles, error happened during pulling the data
print(f"\nError Titles: \n{error_titles}\n")
# A df to store imdb and tmdb titles, and each movie's budget and revenue
budget_revenue = pd.DataFrame(
    {"imdb_title" : imdb_titles,
     "tmdb_titles" : tmdb_titles,
     "budget" : budgets,
     "revenue" : revenues}
)
# Prints budget_revenue and saves budget_revenue and diff to harddrive
print(budget_revenue)
budget_revenue.to_csv("topMovies/budget_revenue.csv")
diff.to_csv("topMovies/diff.csv")

