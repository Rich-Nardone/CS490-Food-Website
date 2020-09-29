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
api = tweepy.API(auth, wait_on_rate_limit=True)

#Set Spoonacular API key to local variable and set url
spoonacular_key = os.environ['SPOON_KEY']
surl = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}".format(spoonacular_key)

#Set of cuisines for complexSearch
cuisines = ['Italian','Chinese','Mexican','Greek','Indian','Japanese','Thai','Cajun','Caribbean','Irish','Korean']

@app.route('/')
def index():
    count = 5
    rnum = random.randint(0,10)
    cuisine = cuisines[rnum]
    recipes = getRecipes(cuisine)
    recipeIDs = getRecipeIDs(recipes)
    results = getTweets(cuisine, count)
    return flask.render_template(
        "index.html",
        #Spoonacular variables
        randnum = random.randint(0,5),
        Cuisine = cuisine,
        SpoonUrl = getSpoonURLs(recipes),
        Recipe = getTitles(recipes),
        Servings = getServings(recipes),
        ReadyTime = getReadyTimes(recipes),
        ImageUrl = getImages(recipes),
        Ingredients = getIngredients(recipeIDs),
        #Tweet variables
        Texts = getTexts(results),
        Users = getUsers(results),
        Times = getTimes(results),
        list_len = count,
        randomtweet = random.randint(0,4)
        )


def getQuery(cuisine):
    query = cuisine+" food -filter:retweets"
    return query

def getTweets(cuisine, count):
    tweets = []
    query = getQuery(cuisine)
    response = api.search(query, count = count, show_user = True, result_type = "recent",lang = "en")
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
        status = api.get_status(tweet.id_str, tweet_mode="extended")
        text = (status.full_text)
        tweets.append(text)
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

def getIngredients(IDs):
    ingred = []
    Lengths = []
    for ID in IDs:
        iurl = "https://api.spoonacular.com/recipes/"+ID+"/ingredientWidget.json?apiKey={}".format(spoonacular_key)
        response = requests.get(iurl)
        json_body = response.json()
        ingredients = []
        Lengths.append(len(json_body["ingredients"]))
        for i in range(0,len(json_body["ingredients"])):
            ingre = json.dumps(json_body["ingredients"][i]["name"])
            ingre = ingre.replace("\"","")
            ingredients.append(ingre)
        ingred.append(ingredients)
    return Lengths, ingred

  
def getRecipes(cuisine):
    response = requests.get(surl+"&cuisine="+cuisine+"&addRecipeInformation=true&number=6")
    return response

def getCuisine():
    r = random.randint(0,10)
    return r
    
def getRecipeIDs(response):
    json_body = response.json()
    IDs = []
    for i in range(0,6):
        IDs.append(json.dumps(json_body["results"][i]["id"]))
    return IDs

def getImages(response):
    json_body = response.json()
    images = []
    for i in range(0,6):
        images.append(json.dumps(json_body["results"][i]["image"]).replace("\"",""))
    return images
    
def getTitles(response):
    json_body = response.json()
    titles = []
    for i in range(0,6):
        titles.append(json.dumps(json_body["results"][i]["title"]).replace("\"",""))
    return titles
    
def getReadyTimes(response):
    json_body = response.json()
    times = []
    for i in range(0,6):
        times.append(json.dumps(json_body["results"][i]["readyInMinutes"]))
    return times
    
def getServings(response):
    json_body = response.json()
    servings = []
    for i in range(0,6):
        servings.append(json.dumps(json_body["results"][i]["servings"]))
    return servings
    
def getSpoonURLs(response):
    json_body = response.json()
    urls = []
    for i in range(0,6):
        urls.append(json.dumps(json_body["results"][i]["spoonacularSourceUrl"]).replace("\"",""))
    return urls
    
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0"),
    debug=True
)