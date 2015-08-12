#! /usr/bin/env python3

import os
import sys
import tweepy

import settings
import logging
import logging.config

def init_logger():
    logging.config.dictConfig(settings.LOGGING)


def oauth_login(consumer_key,
                consumer_secret,
                access_token,
                access_token_secret,
                token_file='auth/twitter.oauth'):
    '''
    Taking a shortcut to use the access tokens directly instead of
    doing the full OAuth procedure. Since I'm the only user of the
    application, that should be fine
    '''
    logging.debug('trying to authenticate with Twitter via OAuth')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)



if __name__ == '__main__':
    init_logger()
    api = oauth_login(settings.TWITTER_CONSUMER_KEY,
                      settings.TWITTER_CONSUMER_SECRET,
                      settings.TWITTER_ACCESS_TOKEN,
                      settings.TWITTER_ACCESS_TOKEN_SECRET)

    # TODO -- use max_id = (last_id)?
    found_tweets = api.search(q='magic origins', count=100)
    for count, tweet in enumerate(found_tweets):
        if tweet.retweet_count > 0:
            print("Retweet ::", count, tweet.text)
        else:
            print("Original ::", count, tweet.text)
