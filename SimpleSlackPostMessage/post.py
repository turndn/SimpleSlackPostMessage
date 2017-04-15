#! /usr/bin/env python
# coding: utf-8

import requests
import json


class SimpleSlackPostMessage(object):
    def __init__(self,
                 token="",
                 channel="",
                 text="",
                 username="",
                 icon_url="",
                 icon_emoji=""):
        with open("settings.json") as f:
            settingsData = json.load(f)

        if not token:
            self.token = settingsData['token']
        else:
            self.token = token

        if not channel:
            self.channel = settingsData['channel']
        else:
            self.channel = channel

        if not username:
            self.username = settingsData['username']
        else:
            self.username = username

        if not icon_url:
            self.icon_url = settingsData['icon_url']
        else:
            self.icon_url = icon_url

        if not icon_emoji:
            self.icon_emoji = settingsData['icon_emoji']
        else:
            self.icon_emoji = icon_emoji

        self.text = text

    # params for postMessage
    def set_param(self):
        if not self.icon_url == "":
            params = {
                'token': self.token,
                'channel': self.channel,
                'text': self.text,
                'username': self.username,
                'icon_url': self.icon_url,
            }
        else:
            params = {
                'token': self.token,
                'channel': self.channel,
                'text': self.text,
                'username': self.username,
                'icon_emoji': self.icon_emoji,
            }
        return params

    def SlackChatPostMessage(self):
        params = self.set_param()
        return self.request_slack_api('chat.postMessage', params)

    def request_slack_api(self, method, params):
        url = 'http://slack.com/api/' + method
        return self.post_request(url, params)

    def post_request(self, url, params):
        response = requests.post(url, params=params, verify=True)
        return response


class SimpleSlackPostUtil(object):
    @staticmethod
    def create_linked_msg(url, text):
        """
        @param: url (string)
        @param: text (string)
        """
        return "<%s|%s>" % (url, text)
