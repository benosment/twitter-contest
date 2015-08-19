import logging
import os
import sqlite3
from datetime import datetime
from contextlib import closing


class Database():
    def __init__(self, db_name, force=False):
        'Set-up a new database, eliminating an old one if it exists'
        self.db_name = db_name
        if force:
            try:
                os.remove(db_name)
            except OSError:
                logging.error('could not remove old database %s' % db_name)
        with closing(sqlite3.connect(db_name)) as c:
            try:
                c.execute('CREATE TABLE tweets (id integer primary key, content text, [timestamp] timestamp)')
                c.execute('CREATE TABLE users (id integer primary key, name text, [timestamp] timestamp)')
            except sqlite3.OperationalError:
                logging.error('could not create database %s' % db_name)


    def add_tweet(self, tweet_id, tweet_content):
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                c.execute('INSERT INTO tweets VALUES (?, ?, ?)',
                          (tweet_id, tweet_content, datetime.now()))
            except sqlite3.OperationalError:
                logging.error('could not insert (%s, %s) into tweets table' %
                              (tweet_id, tweet_content))
            c.commit()


    def get_tweet(self, tweet_id):
        tweet = None
        tweet_id = str(tweet_id)
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                tweet = c.execute('SELECT id FROM tweets WHERE id = ?',
                                  (tweet_id,)).fetchone()
                if tweet:
                    tweet = tweet[0]
            except sqlite3.OperationalError:
                logging.error('query failed')
        return tweet


    def all_tweets(self):
        tweets = None
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                tweets = c.execute('SELECT * FROM tweets').fetchall()
            except sqlite3.OperationalError:
                logging.error('query failed')
        return tweets


    def add_user(self, user_id, user_name):
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                c.execute('INSERT INTO users VALUES (?, ?, ?)',
                          (user_id, user_name, datetime.now()))
            except sqlite3.OperationalError:
                logging.error('could not insert (%s, %s) into users table' %
                              (user_id, user_name))
            c.commit()


    def get_user(self, user_id):
        user = None
        user_id = str(user_id)
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                user = c.execute('SELECT id FROM users WHERE id = ?',
                                 (user_id,)).fetchone()
                if user:
                    user = user[0]
            except sqlite3.OperationalError:
                logging.error('query failed')
        return user


    def all_users(self):
        users = None
        with closing(sqlite3.connect(self.db_name)) as c:
            try:
                users = c.execute('SELECT * FROM users').fetchall()
            except sqlite3.OperationalError:
                logging.error('query failed')
        return users
