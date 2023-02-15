import pandas as pd

data = pd.read_csv("venv/final.csv")

data = data.sort_values("weighted_rating",ascending=False)

output = data[["original_title", "poster_link","release_date","runtime","weighted_rating"]]
