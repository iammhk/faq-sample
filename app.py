#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):

    img_base = "https://raw.githubusercontent.com/svet4/faq-sample/master/img/"

    if req.get("result").get("action") == "topics.authentication":
    
        speech = "You can find your authentication tokens in your agent settings > General > API Keys. Read more here: https://docs.api.ai/docs/authentication."

        display_text = "You can find your authentication tokens in your agent settings > General > API Keys. Read more here: <a href='https://docs.api.ai/docs/authentication' target='_blank'>https://docs.api.ai/docs/authentication</a>."

        pic_url = img_base + "access_tokens.png"

        print("Response:")
        print(speech)

        return {
        "speech": speech,
        "displayText": speech,
        "data": {"pic": pic_url},
        # "contextOut": [],
        "source": "apiai-support-bot"
    }

    else:
        return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
