# project1-Rich-Nardone

Before cloning this repository:

Twitter:
	Sign up for Twitter Developer portal at https://developer.twitter.com
	Once approved enter the portal and navigate to projects and apps.
	Create a new app.
	Click the key symbol to reveal keys and tokens.
Heroku:
	Sign up for heroku at heroku.com

Clone this repository: 
	Use this command to clone repository: git clone http://www.github.com/NJIT-CS490/project1-rmn9
	
Detailed instructions get started:

1. Install python packages by running these commands in terminal:
	pip install tweepy
	pip install flask
	pip install python-dotenv

2. Create file called 'keys.env' and write to the file:
   *** USE THESE VARIABLES AND FILE NAME EXACTLY DO NOT CHANGE **
	export CONSUMER_KEY=''
	export CONSUMER_SECRET=''
	export TOKEN=''
	export TOKEN_SECRET=''

3. In the terminal run the command:
	python main.py
	
4. If on Cloud9 preview templates/index.html. This should render the HTML.

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
	Add your keys and tokens next to their respective variable names.
	
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
	1. Major issue with github and heroku working together. When trying to push to heroku I would recieve fatal errors and my code would not push. 
	   I recieved many error messages pushing and pulling from git aswell. I beleive it was human error from a error in the way I set up each. 
	   I fixed this by starting a new repository and creating a new heroku app and setting it up all over again.
	2. I also had issues parsing the tweepy api responses to get the information for each tweet. I was unable to get the specific time of the tweet.
	   I fixed this by reading the documentation and figuring out that the times were correct but for UTC timezone not ETC.

Issues I am still having with this app:
	1. Coding in HTML and styling with CSS is new to me so I am having trouble getting my code information to display correctly. I am also having trouble 
	   figuring out the styling. I'm going to fix this by reading more documentation on CSS and HTML and most likely do an overhall of the website format and styles.
	2. I am also having trouble navigating the tweepy api responses. I need to read the documentation on how to get the full tweet text adn I would like to have
	   a better understanding of the contents of the JSON response so I can add more information about the tweet like a geotag. This will require me to just read
	   more documentation and experiment.
