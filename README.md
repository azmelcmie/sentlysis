# Twitter Posts Sentiment Analysis 
Python code to demonstrate [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) on Twitter posts (tweets).

# Input & Output
The input will be obtained from Twitter using [Tweepy](http://www.tweepy.org/), a python client for the official Twitter API.
The output will appear on-screen, showing the percentages of positive, neutral and negative tweets along with the content of the last positive and negative tweets. The positive percentage figure will appear in green, neutral in yellow and negative in red.

## Environment
Coded and tested in Anaconda version 4.4.0.

### Libraries

Library | Version
--------| -----------
tweepy| 3.6.0
textblob | 0.15.1
colorama | 0.3.9



## Usage
For you to fetch tweets through the Twitter API, you need to register the app through your Twitter account:
Open this [link](https://apps.twitter.com/) and click the button **Create New App**
Fill the application details. You can leave the callback URL field empty.
Once the app is created you will be redirected to the app page.
Open the **Keys and Access Tokens** tab.
Copy **Consumer Key**, **Consumer Secret**, **Access Token** and **Access Token Secret** and put it in a separate file (conf.py in this case).

conf.py:
````python
# keys and tokens from the Twitter Dev Console
ck = 'Your Consumer Key'
cs = 'Your Consumer Secret'
at = 'Your Access Token'
ats = 'Your Access Token Secret'
````

### Running the program 
From the command line run **python sentlysis.py keyword** where keyword is the subject you want to assess.
The result will appear showing:

>The positive %.   
>The neutral %.  
>The negative %
>
>
>Last assessed positive tweet.  
>Last assessed negative tweet.
<br>
  
You can edit the following line to set the number of tweets to assess. *Don't set too many as you may be blocked by Twitter*.


Change the **count = 200** figure to experiment with different amount of tweets:

**Line 85:** 
````python
tweets = api.get_tweets(query = sys.argv[1] , count = 200)
````


