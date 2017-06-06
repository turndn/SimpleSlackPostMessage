# SimpleSlackPostMessage
This is simple post message script to slack.
[![Build Status](https://travis-ci.org/turndn/SimpleSlackPostMessage.svg?branch=master)](https://travis-ci.org/turndn/SimpleSlackPostMessage)

## Usage
Modify `settings.json` for your environment. (If you have not get slack's token, you check https://api.slack.com/web)

You can post a message only with the following command.

```python
from SimpleSlackPostMessage import SimpleSlackPostMessage, SimpleSlackPostUtil
url = "https://github.com/turndn/SimpleSlackPostMessage"
msg = "This is a message."
text = "%s: %s" % (SimpleSlackPostUtil.create_linked_msg(url, "site"), msg)
SimpleSlackPostMessage(text=text).SlackChatPostMessage()
```
