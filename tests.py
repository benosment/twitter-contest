#! /usr/bin/env python3

import unittest
from unittest.mock import patch, Mock

import tcontest
import settings

from database import Database
from twitter import Twitter

import tweepy

class TwitterUnitTest(unittest.TestCase):

    def setUp(self):
        db = Database('test.db', force=True)
        self.twitter = Twitter(db)

    def test_authenticated(self):
        self.assertEqual(self.twitter.api.me().name, 'Benjamin Osment')

    def test_follow_new_user(self):
        # check create_friendship called
        # check db.all_tweets == 1
        #with patch('tweepy.api.create_friendship') as mock_func:
        #    mock_func.assert_any_calls()
        #self.twitter.api.create_friendship = Mock()
        pass

    def test_follow_old_user(self):
        pass

    def test_retweet_new_tweet(self):
        pass

    def test_retweet_old_tweet(self):
        pass


class DBUnitTest(unittest.TestCase):

    def setUp(self):
        self.db = Database('test.db', force=True)

    def test_add_tweets(self):
        self.db.add_tweet('1', 'hello world')
        self.db.add_tweet('2', 'hello world')
        self.assertEqual(len(self.db.all_tweets()), 2)

    def test_add_users(self):
        self.db.add_user('1', 'jinn')
        self.db.add_user('2', 'steve')
        self.assertEqual(len(self.db.all_users()), 2)

    def test_query_tweet(self):
        self.db.add_tweet('385056910', 'hello world')
        self.assertEqual(self.db.get_tweet('385056910'), 385056910)
        self.assertEqual(self.db.get_tweet('3'), None)

    def test_query_users(self):
        self.db.add_user('385056910', 'jinn')
        self.assertEqual(self.db.get_user('385056910'), 385056910)
        self.assertEqual(self.db.get_user('3'), None)


if __name__ == '__main__':
    unittest.main()
