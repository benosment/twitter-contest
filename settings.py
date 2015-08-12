import os


TWITTER_APP_NAME = os.environ.get('TWITTER_APP_NAME')
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] [%(funcName)s:%(lineno)d] %(message)s',
            'datefmt':'%m/%d/%Y %I:%M:%S %p',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'log.txt',
            'formatter': 'standard'
        },
    },

    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        }
    }
}
