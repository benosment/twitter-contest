import logging
import tweepy
import settings


class Twitter():
    def __init__(self, db):
        self.db = db
        self.api = self.oauth_login(settings.TWITTER_CONSUMER_KEY,
                                    settings.TWITTER_CONSUMER_SECRET,
                                    settings.TWITTER_ACCESS_TOKEN,
                                    settings.TWITTER_ACCESS_TOKEN_SECRET)


    def oauth_login(self,
                    consumer_key,
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

    def rate_limit_stats(self):
        logging.debug('API rate limiting status', self.api.rate_limit_status())

    def search(self, query):
        found_tweets = self.api.search(q=query, count=100, lang='en')
        for count, tweet in enumerate(found_tweets):
            if hasattr(tweet, 'retweeted_status'):
                logging.debug("Retweet :: %d %s" % (count, tweet.text))
                logging.debug("Original tweet was from %s and was %s" %
                              (tweet.retweeted_status.user.screen_name,
                               tweet.retweeted_status.text))
                if ('RT' in tweet.retweeted_status.text):
                    logging.debug("!!! Candidate for contest")
                    import pdb; pdb.set_trace()
                    if ('follow' in tweet.retweeted_status.text.lower()):
                        self.follow(tweet.retweeted_status.user.screen_name)
                    self.retweet(tweet)
            else:
                print("Original :: %d %s" % (count, tweet.text))

    def follow(self, user):
        # TODO -- need to check if we have been friends before
        self.api.create_friendship(user)
        logging.debug('started following %s' % user)

    def unfollow(self, user):
        pass

    def retweet(self, tweet):
        # TODO -- need to check if we have tweeted this ID before
        self.api.retweet(tweet.retweeted_status.id)
        logging.debug('retweeted %d : %s' % (tweet.retweeted_status.id,
                                             tweet.retweeted_status.text))
