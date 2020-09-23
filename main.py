import tweepy
import os
import flask
import random
import json
import datetime

from os.path import join, dirname
from dotenv import load_dotenv

app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'keys.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("TOKEN")
access_token_secret = os.getenv("TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

food_items = ['potatoes','broccoli','garlic','tomatoes','pasta','tacos','ice cream','chocolate']

@app.route('/')
def index():
    count = 5
    query = food_items[random.randint(0,7)]
    results = getTweets(query, count)
    texts = getTexts(results)
    times = getTimes(results)
    users = getUsers(results)
    return flask.render_template(
        "index.html",
        Texts = texts,
        Users = users,
        Times = times,
        list_len = count
        )
def getUsers(results):
    users = []
    for tweet in results:
        users.append(tweet.user.name)
    return users
    
def getTexts(results):
    tweets = []
    for tweet in results:
        tweets.append(tweet.text)
    return tweets
    
def getTweets(query, count):
    response = api.search(query, count = count, show_user = True, lang = "en")
    tweets = []
    for tweet in response:
        tweets.append(tweet)
    return tweets
    
def getTimes(results):
    times = []
    for tweet in results:
        time = tweet.created_at
        year = str(time.year)
        month = str(time.month)
        day = str(time.day)
        hour = str((time.hour))
        minute = str(time.minute)
        second = str(time.second)
        holder = month+'/'+day+'/'+year+' at '+hour+':'+minute+':'+second+ ' UCT'
        times.append(holder)
    return times
    
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)