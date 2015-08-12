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

    logging.debug('trying to authenticate with Twitter via OAuth')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
    print(api.me().name)


if __name__ == '__main__':
    init_logger()
    oauth_login(settings.TWITTER_CONSUMER_KEY,
                settings.TWITTER_CONSUMER_SECRET,
                settings.TWITTER_ACCESS_TOKEN,
                settings.TWITTER_ACCESS_TOKEN_SECRET)
