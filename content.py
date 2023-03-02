""""import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("/Users/simijindal/Desktop/whjjr program/movie reccomendation flask/PRO-C141-Student-Activity-master/venv/final.csv")
df = df["soup"]
print(df)
df = df[df["soup"].notna()]
counter = CountVectorizer(stop_words="english")
counter_new = counter.fit_transform(df["soup"])
cosine = cosine_similarity(counter_new,counter_new)
df = df.reset_index()
indices = pd.Series(df.index,index=df["original_title"])
def get_movie(title):
    idx = indices["title"]
    score = list(enumerate(cosine[idx]))
    score = sorted(score,key=lambda x: x[1],reverse=True)
    score = score[1:11]
    movies_list = [i[0] for i in score]
    return df[["original_title", "poster_link","release_date","runtime","weighted_rating"]].iloc[movies_list]

print(get_movie("Avatar"))
""""