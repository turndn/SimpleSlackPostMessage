#! /usr/bin/env python2
# coding: utf-8
import slack_postMessage

if __name__ == '__main__':
    res = slack_postMessage.simpleSlackPostMessage(text=u"test string").slackChatPostMessage()
    print res
