#! /usr/bin/env python3

import os
import sys
import settings
import logging
import logging.config
from database import Database
from twitter import Twitter

def init_logger():
    logging.config.dictConfig(settings.LOGGING)


if __name__ == '__main__':
    init_logger()
    db = Database('tweet.db')
    t = Twitter(db)
    t.search('RT win')
