import tweepy
from textblob import TextBlob
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def authenticate_twitter_app():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def analyze_tweets(query):
    api = authenticate_twitter_app()
    tweets = api.search(q=query, count=100, lang='en')
    
    tweet_data = []
    sentiment_scores = {'positive': 0, 'negative': 0, 'neutral': 0}
    
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment.polarity
        tweet_data.append({'text': tweet.text, 'sentiment': sentiment})
        
        if sentiment > 0:
            sentiment_scores['positive'] += 1
        elif sentiment < 0:
            sentiment_scores['negative'] += 1
        else:
            sentiment_scores['neutral'] += 1
            
    return tweet_data, sentiment_scores
