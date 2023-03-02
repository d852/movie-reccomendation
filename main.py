from flask import Flask, jsonify
import pandas as pd
from  popular import output
"""from content import get_movie"""


df= pd.read_csv('/Users/simijindal/Desktop/whjjr program/movie reccomendation flask/PRO-C141-Student-Activity-master/venv/final.csv')

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
@ app.route("/liked_movies")
def liked():
  global all_movies
  movies_list = store_variable()
  liked_movies.append(movies_list)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "message":'success'
  })


@ app.route("/like")
def liked_list():
  global liked_movies
  return jsonify({
    "data":liked_movies,
    "message":"success"
  })
# /movies api


# /like api


# /dislike api
@ app.route("/disliked_movies")
def disliked():
  global all_movies
  movies_list = store_variable()
  unliked_movies.append(movies_list)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "message":'success'
  })


# /did_not_watch api
@ app.route("/not_watched_movies")
def not_watched_movies():
  global all_movies
  movies_list = store_variable()
  did_not_watch_movies.append(movies_list)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop=True)
  return jsonify({
    "message":'success'
  })


"""@ app.route("/recommended")
def recommended():
  global liked_movies
  colum_names = ["original_title", "poster_link","release_date","runtime","weighted_rating"]
  recommend = pd.DataFrame(columns=colum_names)
  for i in liked_movies:
    out = get_movie(i["original_title"])
    recommend = recommend.append(out)
  recommend.drop_duplicates(subset=["original_title"],inplace=True)
  recommend_data = []
  for i,row in recommend.iterrows():
    r_movies = {
      "original_title":row["original_title"],
      "poster_link":row["poster_link"],
      "release_date":row['release_date'],
      "runtime":row['runtime'],
      "weighted_rating":row['weighted_rating']
    }
    recommend_data.append(r_movies)
"""

if __name__ == "__main__":
  app.run()