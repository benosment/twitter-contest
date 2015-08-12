#! /usr/bin/env python3

import unittest

import tcontest
import settings


class TwitterUnitTest(unittest.TestCase):
    def setUp(self):
        self.api = tcontest.oauth_login(settings.TWITTER_CONSUMER_KEY,
                                        settings.TWITTER_CONSUMER_SECRET,
                                        settings.TWITTER_ACCESS_TOKEN,
                                        settings.TWITTER_ACCESS_TOKEN_SECRET)

    def test_authenticated(self):
        self.assertEqual(self.api.me().name, 'Benjamin Osment')


if __name__ == '__main__':
    unittest.main()
