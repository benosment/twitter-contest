#! /usr/bin/env python3

import os
import sys

import logging
import logging.config


def init_logger():
    logging.config.dictConfig(settings.LOGGING)


if __name__ == '__main__':
    init_logger()
    db = Database('tweet.db')
    t = Twitter(db)

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
