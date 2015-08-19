#! /usr/bin/env python3

import os
import sys
import tweepy
import settings
import logging
import logging.config


def init_logger():
    logging.config.dictConfig(settings.LOGGING)


def get_user(user_id):
    user = None
    with closing(sqlite3.connect(database)) as c:
        try:
            tweet = c.execute('SELECT id FROM users WHERE id = ?',
                              user_id).fetchone()
        except sqlite3.OperationalError:
            logging.error('query failed')
    return user


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
    db = Database('tweet.db')
    # api = oauth_login(settings.TWITTER_CONSUMER_KEY,
    #                   settings.TWITTER_CONSUMER_SECRET,
    #                   settings.TWITTER_ACCESS_TOKEN,
    #                   settings.TWITTER_ACCESS_TOKEN_SECRET)

    # # TODO -- returns nothing?
    # logging.debug('API rate limiting status', api.rate_limit_status())

    # # TODO -- use max_id = (last_id)?
    # found_tweets = api.search(q='RT win', count=100, lang='en')
    # for count, tweet in enumerate(found_tweets):
    #     if hasattr(tweet, 'retweeted_status'):
    #         print("Retweet :: %d %s" % (count, tweet.text))
    #         print("Original tweet was from %s and was %s" %
    #               (tweet.retweeted_status.user.screen_name, tweet.retweeted_status.text))
    #         if ('RT' in tweet.retweeted_status.text):
    #             print("!!! Candidate for contest")
    #             # TODO -- need to check if we have been friends before
    #             # TODO -- need to check if we have tweeted this ID before
    #             import pdb; pdb.set_trace()
    #             api.create_friendship(tweet.retweeted_status.user.screen_name)
    #             logging.debug('started following %s' % tweet.retweeted_status.user.screen_name)
    #             api.retweet(tweet.retweeted_status.id)
    #             logging.debug('retweeted %d : %s' % (tweet.retweeted_status.id,
    #                                                  tweet.retweeted_status.text))
    #     else:
    #         print("Original :: %d %s" % (count, tweet.text))
