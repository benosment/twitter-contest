#! /usr/bin/env python3

import unittest

import tcontest
import settings

from database import Database

class TwitterUnitTest(unittest.TestCase):

    def setUp(self):
        self.api = tcontest.oauth_login(settings.TWITTER_CONSUMER_KEY,
                                        settings.TWITTER_CONSUMER_SECRET,
                                        settings.TWITTER_ACCESS_TOKEN,
                                        settings.TWITTER_ACCESS_TOKEN_SECRET)

    def test_authenticated(self):
        self.assertEqual(self.api.me().name, 'Benjamin Osment')


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
        self.db.add_tweet('1', 'hello world')
        self.assertEqual(self.db.get_tweet('1'), 1)
        self.assertEqual(self.db.get_tweet('3'), None)

    def test_query_users(self):
        self.db.add_user('1', 'jinn')
        self.assertEqual(self.db.get_user('1'), 1)
        self.assertEqual(self.db.get_user('3'), None)


if __name__ == '__main__':
    unittest.main()
