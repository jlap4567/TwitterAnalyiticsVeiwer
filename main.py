import tweepy #allows the program to interact with twitter api
import csv #allows program to create a csv file to use as a database
import datetime #allow program to get the current date and time
import os #allows program to operate using mac os commands
import time #allows program to wait for an amount of time
import threading #allows the program to run multithreaded

#Keys to access twitter account
CONSUMER_KEY = 'bz5MIgTVltSAGrOVRwTEBJFgm'
CONSUMER_SECRET = 'sfMSclxsco6A34DqPEUok2hAifIzhZs7mrPGOcYvFNRKreZuHf'
ACCESS_KEY = '1061740751288262658-PHkUt0Hs3myAj1cCmsvWRmSu2THOR5'
ACCESS_SECRET = 'DO5Dr8L3UWGI7IelaByq78tjC9ANcSDXttZmlGGl0EUyc'

#Uses twitter keys
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

keyword = 'Trump'

tweets = {}

def getPosts():
    """
    Collects 100 posts with Floridaman Hashtag from today
    and saves them in a csv file
    """
    global keyword
    #Gets and formats todays date
    now = datetime.datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

    for tweet in tweepy.Cursor(api.search,q=keyword,count=10,lang="en",
                                            since=date).items():
        tweets[tweet.id] = [tweet.created_at,tweet.coordinates]

def main():
    keyword = "Trump"
    getPosts()
    print(tweets)


if __name__ == '__main__':
    main()
