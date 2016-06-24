import sys
from termcolor import colored
usage = "You must type : python %s filename.xlsx"
if len(sys.argv) != 2:
    print >> sys.stderr, \
    colored(usage % sys.argv[0], "yellow")
    sys.exit(1)

import pyexcel as excel
import pyexcel.ext.xls
from twitter_data import TwitterAPI
from datetime import timedelta, date
from termcolor import colored
import json, pickle
import tweepy
import csv


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

    def get_tweets(self,hashtag):
        data = []
        for tweet in tweepy.Cursor(self.api.search, q=hashtag).items(10):
            print tweet.text
            data.append(tweet.text)
        return data

    def get_data(self):
        '''Abre un archivo .xlsx y obtiene las dos columnas (usuario y fecha) obtiene los datos de before during y after del evento'''
        data = excel.get_records(file_name=sys.argv[1])
        users,dates = ({} for i in range(2))
        metadata = {}
        tweets = {}
        for record in data:
            hashtag = record['Hashtag']
            if hashtag != 'none' and hashtag != '' and '#' in hashtag:
                if not tweets.has_key(hashtag):
                    print hashtag
                    t = self.get_tweets(hashtag)
                    tweets.update({hashtag:t})
            else:
                pass
        print tweets


    def storePickle(metadata):
        output = open('results.pkl', 'wb')
        pickle.dump(metadata, output)
        output.close()

t = TwitterAPI()
t.get_data()
