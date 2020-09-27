import tweepy
import os
import flask
import random
import json
import datetime
import requests
from os.path import join, dirname
from dotenv import load_dotenv

app = flask.Flask(__name__)

#Load keys via keys.env
dotenv_path = join(dirname(__file__), 'keys.env')
load_dotenv(dotenv_path)

#set Twitter API keys to local variables
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("TOKEN")
access_token_secret = os.getenv("TOKEN_SECRET")

#OAuth for Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Set Spoonacular API key to local variable and set url
spoonacular_key = os.environ['SPOON_KEY']
surl = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}".format(spoonacular_key)

#Set of cuisines for complexSearch
state = ['Italian','Chinese','Mexican','German','Indian','Japanese','French']

#
response = requests.get(surl+"&cuisine="+state[random.randint(0,6)]+"&addRecipeInformation=true")
json_body = response.json()
recipeID = json.dumps(json_body["results"][0]["id"])


@app.route('/')
def index():
    rnum = random.randint(0,6)
    count = 5
    query = state[rnum]
    response = requests.get(surl+"&cuisine="+state[rnum]+"&addRecipeInformation=true")
    json_body = response.json()
    recipeID = json.dumps(json_body["results"][0]["id"])
    ingredients = getIngredients(recipeID)
    results = getTweets(query, count)
    texts = getTexts(results)
    times = getTimes(results)
    users = getUsers(results)
    return flask.render_template(
        "index.html",
        Texts = texts,
        Users = users,
        Times = times,
        list_len = count,
        Ingredients = ingredients,
        ilen = len(ingredients)
        )
        
def getTweets(query, count):
    response = api.search(query, count = count, show_user = True, lang = "en")
    tweets = []
    for tweet in response:
        tweets.append(tweet)
    return tweets

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

def getIngredients(ID):
    iurl = "https://api.spoonacular.com/recipes/"+ID+"/ingredientWidget.json?apiKey={}".format(spoonacular_key)
    response = requests.get(iurl)
    json_body = response.json()
    ingredients = []
    for i in range(0,len(json_body["ingredients"])):
        ingredients.append(json.dumps(json_body["ingredients"][i]["name"]))
        
    return ingredients
    
print(getIngredients(recipeID))
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)