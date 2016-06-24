import tweepy, time, datetime, json
import pickle


class TwitterAPI:
    def __init__(self):

        consumer_key = "UBXxFjvDkOXjkzEsTEPDwjrFM"
        consumer_secret = "fKN816JlcG7fp5DqqhAoND0zBJxrkOONIAHYIuZUUGkFYtKxPU"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "743541971604635648-NYjye8ABjHY2yTbhrcSeHW7a2lqprlA"
        access_token_secret = "8qJfTUJV1rVY3Ua8p9NetuMLNlZAAnY08mHn78Vxxe0e7"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    def spread_article(self,sname, tweetId):
        text = "  Hey @"+sname+ ", I hear that you are an expert on this area, can you give me some feedback? https://goo.gl/l9iuoX"
        self.api.update_status(text,tweetId)

    def get_tweets(self):
        tweetIdx = []
        snamex = []
        for tweets in tweepy.Cursor(self.api.search, q='Every Day David Levithan').items(10):
            print tweets.text
            snamex.append(tweets.author._json['screen_name'])
            tweetIdx.append(tweets.id)
        return snamex,tweetIdx
