from flask import Flask
from flask import jsonify
from flask import request
import LM35

app = Flask(__name__)

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
# fetch action from json
    action = req.get('queryResult').get('action')
    temp_now = "Temperature now: " + str(LM35.temperature()) + "C"
# return a fulfillment response
    r = {
  "fulfillmentText": "Text response",
  "fulfillmentMessages": [
    {
      "text": {
        "text": [temp_now]
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
              "textToSpeech": temp_now,
              "displayText": temp_now
            }
          }
        ]
      }
    }
  }
}
    return r
# create a route for webhook
@app.route('/webhook/temp', methods=['GET', 'POST'])
def webhook():
    # return response
    return jsonify(results())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)