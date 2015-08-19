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
