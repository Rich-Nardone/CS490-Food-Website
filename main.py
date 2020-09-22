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
    
    query = food_items[random.randint(0,7)]
    results = getTweets(query, 3)
    return flask.render_template(
        "index.html",
        Results = results,
        list_len = 3
        )
        
        
def getTweets(query, count):
    response = api.search(query, count = count, show_user = True, lang = "en")
    tweets = []
    for tweet in response:
        time = getTime(tweet.created_at)
        tweets.append(str(tweet.user.name) + ' tweeted: "' + tweet.text + '" at: ' +str(tweet.created_at.month) +' '+str(tweet.created_at.day)+', '+str(tweet.created_at.year)+', '+time)
    return tweets
    
def getTime(time):
    hour = str((time.hour - 4) % 12)
    minute = str(time.minute)
    second = str(time.second)
    return (hour+':'+minute+':'+second+' EST' )
    
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)