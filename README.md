# simpleSlackPostMessage
This is simple post message script to slack.

## Usage
Modify `settings.json` for your environment. (If you have not get slack's token, you check https://api.slack.com/web)

You can post a message only with the following command.


  import slack_postMessage
  slack_postMessage.simpleSlackPostMessage(text=u"test string").slackChatPostMessage()
