import conf
import re
import tweepy
import sys
from colorama import init
from colorama import Fore, Back, Style
from tweepy import OAuthHandler
from textblob import TextBlob

# Colorama initialisation required for Windows
init()
 
class TwitterClient(object):
    # Generic Twitter Class for sentiment analysis
    def __init__(self):
        # keys and tokens from the Twitter Dev Console
        consumer_key = conf.ck
        consumer_secret = conf.cs
        access_token = conf.at
        access_token_secret = conf.ats
 
        # Authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        # Cleaning tweet text by removing links / special characters using regex
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        # Using textblob sentiment method to classify sentiment
        analysis = TextBlob(self.clean_tweet(tweet))
        # Set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        # Empty list to store parsed tweets
        tweets = []
 
        try:
            # Call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
 
            # Parsing tweets one by one
            for tweet in fetched_tweets:
                # Empty dictionary to store required parameters of a tweet
                parsed_tweet = {}
 
                # Saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # Appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # If tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # Return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # Print error (if any)
            print("Error : " + str(e))
 
def main():
    # Creating object of TwitterClient Class
    api = TwitterClient()
    # Calling function to get tweets
    tweets = api.get_tweets(query = sys.argv[1] , count = 200)
    print()
    print("Sentiment Analysis Result for: %s \n" % (sys.argv[1]))
    # Picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # Percentage of positive tweets in green
    print(Style.RESET_ALL, Style.BRIGHT, "Positive tweets percentage:", Fore.GREEN + "{0:.2f} %".format(100*len(ptweets)/len(tweets)))
    # Picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # Percentage of neutral tweets in yellow
    print(Style.RESET_ALL, Style.BRIGHT, "Neutral tweets percentage:", Fore.YELLOW + "{0:.2f} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    # Percentage of negative tweets in red
    print(Style.RESET_ALL, Style.BRIGHT, "Negative tweets percentage:", Fore.RED + "{0:.2f} %".format(100*len(ntweets)/len(tweets)))
    # Reset color to default
    print(Style.RESET_ALL)
    
    # Printing first x positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:1]:
        print(tweet['text'])
 
    # Printing first x negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:1]:
        print(tweet['text'])
 
if __name__ == "__main__":
    main()