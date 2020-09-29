# project1-Rich-Nardone

Before cloning this repository:

Twitter:
	Sign up for Twitter Developer portal at https://developer.twitter.com
	Once approved enter the portal and navigate to projects and apps.
	Create a new app.
	Click the key symbol to reveal keys and tokens.
	*** These keys are private do not show them to others ***
Heroku:
	Sign up for heroku at heroku.com
Spoonacular:
	Sign up for Spoonacular api at https://spoonacular.com/food-api/console#Dashboard
	Navigate to My Console then click Profile
	Click the pink button Show/Hide API key to reveal your key
	*** These keys are private do not show them to others ***

Clone this repository: 
	Use this command to clone repository: git clone http://www.github.com/NJIT-CS490/project1-rmn9
	
Detailed instructions get started:

1. Install python packages by running these commands in terminal:
	pip install tweepy
	pip install flask
	pip install python-dotenv

2. Create file called 'keys.env' and write to the file:
   *** USE THESE VARIABLES AND FILE NAME EXACTLY DO NOT CHANGE ***
   *** Replace TODO in each line with its respective Twitter api key ***
   *** Replace TODO in the line containing SPOON_KEY with your spoonacular api key ***
	export CONSUMER_KEY='TODO'
	export CONSUMER_SECRET='TODO'
	export TOKEN='TODO'
	export TOKEN_SECRET='TODO'
	export SPOON_KEY='TODO'

	
3. In the terminal run the command:
	python main.py
	
4. If on Cloud9 preview templates/index.html. This should render the HTML.
	In the terminal hit CTRL+C to end the script in Cloud9

5. Install heroku:
	npm install -g heroku
	heroku login -i
	heroku create
	git push heroku master

6. Get heroku set up.
	Navigate to your heroku dashboard at https://dashboard.heroku.com/apps
	Click on your newly created app and navigate to settings.
	Scroll down to Config Vars and click Reveal Config Vars.
	Add your key values and tokens we retrieved from twitter.
	Name your config vars exactly the same:
		CONSUMER_KEY
		CONSUMER_SECRET
		TOKEN
		TOKEN_SECRET
		SPOON_KEY
	Add your keys and tokens from your keys.env file next to their respective variable names.
	
7. Configure requirements.txt with all requirements needed to run your app.
	For this app all thats needed is:
		Flask
		python-dotenv
		tweepy

8. Configure Procfile with the command needed to run your app.
	For this app all thats needed is:
		web: python main.py

9. If you are still having issues, you may use heroku logs --tail to see what's wrong.
	
	
Issues I had creating this app:
	1. I wanted to make the app more organized in terms of API calls and responses. The calls and responses crowded the top of my index function. I created functions 
	   to organize my api calls for both twitter and spoonacular but the spoonacular functions were acting weird giving completely wrong data. I figured out I needed to 
	   remove json.dumps() the getRecipes() function and use it in each function I called to retrieve spoonacular data. I had this error because of a lack of understanding 
	   and experience working with json files in python. Reading up on some documentation solved my issues aswell as trial and error.
	2. I had trouble with the ingredients section of the spoonacular response. This was before I had figured out the best way to parse through the spoonacular json response 
	   in a function with the response as a parameter. I solved this by using another query in spoonacular which allows you to search for the ingredients of a recipe by
	   its id tag. This fix and secondary search query using the ID may be irrelevant now that I have fixed the underlying issue which was the json.dumps problem but
	   the code works fine with it.
	3. Another issue I had trouble with was tweets displayed multiple times if the same cuisine was selected. Often times a new recipe would load on the screen but it would 
	   be the same cuisine ie. Chinese but the tweet would be the same becuase I was searching for tweets based on the cuisine and I was only asking for one tweet. I fixed this by 
	   reading through the Twitter API Docs and finding the search request and reading its optional parameters. One of the parameters I found useful was the count parameter which allowed 
	   me to specify how many tweets I wanted in response. I experimented with different amounts of tweets and another paramter which allowed your to specify the type of tweet.
	   The type of tweet parameter had three options 'popular','mixed' and 'recent'. Finally I put the tweets into an array and used a random number to select which tweet I would display
	   on each load.

Issues I am still having with this app:
	1. After implementing final functions to organize my code and declutter the index() function I found my app in the c9 preview and browser preview load very slowly.
	   I understand this issue could be fixed by hardware upgrades and deploying my app from a local machine instead of heroku. To fix this issue without hardware changing 
	   I would go through my code and eliminate code which is unneccesary or restructure my code to use less function calls. That fix would shave little time off my load 
	   speed. Another fix I would use would be eliminating the second spoonacular api call for ingredients and restruct the code to grab ingredients from the original response.
	2. If I had more time I would also learn more about the twiter queries and how to format queries which would result in better tweets. Currently my queries just filter out 
	   retweets and search for tweets containing a phrase cuisine+" food" substituting cuisine for a string identifying a specific food origin like American, Chinese, Indian, Greek.
	   Twitter currently offers a variety of search operator to narrow or widen your search at https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/overview/standard-operators
	   I was expecting twitter to use regex for queries but after finding this out I would experiment with these operators because my tweets were sometimes off topic.
