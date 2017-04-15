#! /usr/bin/env python
# coding: utf-8
from SimpleSlackPostMessage import SimpleSlackPostMessage, SimpleSlackPostUtil

if __name__ == '__main__':
    url = "https://github.com/turndn/SimpleSlackPostMessage"
    msg = "This is a message."
    text = "%s: %s" % (SimpleSlackPostUtil.create_linked_msg(url, "site"), msg)
    res = SimpleSlackPostMessage(text=text).SlackChatPostMessage()
