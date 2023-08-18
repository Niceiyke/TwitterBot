import os
import tweepy

from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class TweetBotConfig:
    load_dotenv()

    TWEET_API_KEY=os.getenv('API_kEY')
    TWEET_SECRET_KEY =os.getenv('SECRET_KEY')
    TWEET_BEARER_TOKEN =os.getenv("BEARER_TOKEN")
    TWEET_ACCESS_TOKEN= os.getenv("ACCESS_TOKEN")
    TWEET_ACCESS_SECRET= os.getenv("ACCESS_TOKEN_SECRET")
    TWWET_BEARER_TOKEN = os.getenv("BEARER_TOKEN")





class TweetBot:

    def __init__(self) -> None:
        auth =tweepy.Client(bearer_token=TweetBotConfig.TWWET_BEARER_TOKEN, consumer_key=TweetBotConfig.TWEET_API_KEY,consumer_secret= TweetBotConfig.TWEET_SECRET_KEY,access_token= TweetBotConfig.TWEET_ACCESS_TOKEN,access_token_secret= TweetBotConfig.TWEET_ACCESS_SECRET)
        self.client =tweepy.Client(bearer_token=TweetBotConfig.TWWET_BEARER_TOKEN, consumer_key=TweetBotConfig.TWEET_API_KEY,consumer_secret= TweetBotConfig.TWEET_SECRET_KEY,access_token= TweetBotConfig.TWEET_ACCESS_TOKEN,access_token_secret= TweetBotConfig.TWEET_ACCESS_SECRET)
        

    

    def create_tweet(self,tweet):

        self.client.create_tweet(text=tweet)

        print('Tweet Posted')

if __name__=="__main__":

    bot=TweetBot()

    bot.create_tweet(tweet="I love being married. It's so great to find that one special person you want to annoy for the rest of your life.—Rita Rudner")
