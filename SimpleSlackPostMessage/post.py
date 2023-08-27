#! /usr/bin/env python
import requests
import json


class SimpleSlackPostMessage(object):
    def __init__(self, path, url=""):
        with open(f"{path}/settings.json") as f:
            settingsData = json.load(f)

        if not url:
            self.url = settingsData['url']
        else:
            self.url = url

    # params for postMessage
    def set_param(self, text):
        params = {'text': text}
        return params

    def SlackChatPostMessage(self, text):
        params = self.set_param(text)
        return self.request_slack_api(params)

    def request_slack_api(self, payload):
        url = self.url
        return self.post_request(url, payload)

    def post_request(self, url, payload):
        response = requests.post(url, json=payload)
        return response


class SimpleSlackPostUtil(object):
    @staticmethod
    def create_linked_msg(url, text):
        """
        @param: url (string)
        @param: text (string)
        """
        return "<%s|%s>" % (url, text)
