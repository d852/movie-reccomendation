from flask import Flask, jsonify
import pandas as pd
from  popular import output

df= pd.read_csv('venv/final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies  = df[["original_title", "poster_link","release_date","runtime","weighted_rating"]]


# variables to store data
liked_movies= []
unliked_movies= []
did_not_watch_movies= []


def store_variable():
  movie_data = {"original_title":all_movies.iloc[0,0],"poster_link":all_movies.iloc[0,1],"release_date":all_movies.iloc[0,2] or "NA","runtime":all_movies.iloc[0,3],"weighted_rating":all_movies.iloc[0,4]/2}
  return movie_data



@ app.route('/')
def movies():
  return jsonify({
    "data":store_variable(),
    "message":"success"  
  })


@ app.route('/popular_movies')
def popular_movies():
  p_movies_list = []
  for i,row in output.iterrows():
    p_movies = {
      "original_title":row["original_title"],
      "poster_link":row["poster_link"],
      "release_date":row['release_date'],
      "runtime":row['runtime'],
      "weighted_rating":row['weighted_rating']
    }
    p_movies_list.append(p_movies)
  print(p_movies_list)

  return jsonify({
    "data":p_movies_list,
    "message":"success"
  })




# method to fetch data from database


# /movies api


# /like api


# /dislike api


# /did_not_watch api


if __name__ == "__main__":
  app.run()