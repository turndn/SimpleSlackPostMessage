#! /usr/bin/env python

from SimpleSlackPostMessage import SimpleSlackPostMessage, SimpleSlackPostUtil
from unittest import main, TestCase

import os

APIKEY = os.environ['API_KEY']


class TestPost(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all(self):
        url = "https://github.com/turndn/SimpleSlackPostMessage"
        msg = "This is a message."
        text = "%s: %s" % (
            SimpleSlackPostUtil.create_linked_msg(url, "site"), msg)
        s = SimpleSlackPostMessage(token=APIKEY,
                                   channel="#random",
                                   username="test",
                                   text=text)
        self.assertEqual(s.SlackChatPostMessage().status_code, 200)


if __name__ == '__main__':
    main()
