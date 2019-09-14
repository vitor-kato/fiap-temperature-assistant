# Project to run a temperature check over google assistant

### Components used

* MCP3008
* LM35
* Raspberry pi 3B

### How it works

First we need to open a outside route for our raspberry, so we can access it from the internet.
Here we used [Remote.it](https://remote.it) to open the path.
But you can use ngrok or similar.

We run a flask server to run the script to get the temperature value from the LM35
sensor while doing the proper convertions.

On the DialogFlow dashboard, we create the intent and user phrases so our Google Assistant Bot
run the query to our webserver via a webhook

Then we format the response, so DialogFlow can parse it and display to the user, over text and TTS


### Diagram

![Alt text](diagram.jpg?raw=true "Diagram")

