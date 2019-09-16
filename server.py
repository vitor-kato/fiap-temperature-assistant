#!/usr/bin/env python3

# running in Remote.it

from flask import Flask
from flask import jsonify
from flask import request
from relay import switch_relay
import sys
import logging
import LM35

app = Flask(__name__)


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

# fetch action from json
    action = req.get('queryResult').get('intent').get('displayName')

# return a fulfillment response
    if action == 'check-temp':
      temp_now = "Temperature now: " + str(LM35.temperature()) + "C"
      r = fulfillment_template(temp_now)
    else:
      switch_relay()
      r = fulfillment_template('Light Switched')
    return r


def fulfillment_template(data):
  template = {
        "fulfillmentText": "Text response",
        "fulfillmentMessages": [
          {
            "text": {
              "text": [data]
            }
          }
        ],
        "source": "room-temperature",
        "payload": {
          "google": {
            "expectUserResponse": True,
            "richResponse": {
              "items": [
                {
                  "simpleResponse": {
                    "textToSpeech": data,
                    "displayText": data
                  }
                }
              ]
            }
          }
        }
      }
  return template

# create a route for webhook
@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    # if intent is 'check-temp'
    # return response
    return jsonify(results())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)