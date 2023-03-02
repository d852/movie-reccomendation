import pandas as pd

data = pd.read_csv("/Users/simijindal/Desktop/whjjr program/movie reccomendation flask/PRO-C141-Student-Activity-master/venv/final.csv")

data = data.sort_values("weighted_rating",ascending=False)

output = data[["original_title", "poster_link","release_date","runtime","weighted_rating"]]
