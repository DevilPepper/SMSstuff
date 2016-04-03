from flask import Flask, request, redirect
import twilio.twiml
import json
import sys
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import contextlib
import urllib
import urllib2
import requests

theList = []
inputs = []

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #"""Respond to incoming calls with a simple text message."""
 
    txt = request.args.get('MessageSid', '')
    resp = twilio.twiml.Response()
    
    account_sid = "ACd56262f209cd94fe377106f857bd8f82"
    auth_token  = "2c0d255b6ad344bca74537fd5ca022c9"
    
    #account_sid = "ACf0ce6e03499a2da7d37621c539f804c7"
    #auth_token  = "41e7d0631589238c7c5d9c62b28c47d2"

    client = TwilioRestClient(account_sid, auth_token)
 
    sms = client.messages.get(txt)

    #if(p# !exist)
    #create it in db
    #get val for p#

    if sms.from_ in inputs:
        inputs[inputs.index(sms.from_) + 1] = " ".join([inputs[theList.index(sms.from_) + 1], sms.body])
    else:
        inputs.append(sms.from_)
        inputs.append(sms.body)

    cmd = ""
    cmd += inputs[inputs.index(sms.from_) + 1].lower()
    
    #print sms.from_
    tokens = cmd.split()

    #if any(x["p"] == sms.from_ for x in theList):
    found=False
    player = {}

    for i in theList :
        if i["p"] == sms.from_ :
            found = True
            i["trys"] -= 1
            #tries = i["trys"]
            player = i
            if i["trys"] <= 0 :
                theList.remove(i)

    if found:
        #play game
        if tokens[0] in player["tags"]:
            output = "You got it!! Here's the image url: " + player["img"]
        else:
            output = "Aww. You've got " + str(player["trys"]) + " tries left"
        resp.message(output)

    else:
        with open('state.json') as data_file:    
            statesJSON = json.load(data_file)

        for token in tokens :
            if token == "call" or token == "0" or not token.isdigit() :
                break
            else :
                if int(token) <= len(statesJSON) :
                    statesJSON = statesJSON[int(token)-1]["sub"]

        output = ""
        end = ""
        for i in statesJSON :
            if i["text"] == "sonic" or i["text"] == "merchant" or i["text"] == "gif" :
                output = i["url"]
                end = i["text"]
                break
            output += i["text"] + "\n"


        #elif  :


    #print sms.body
    
    #theList.append(56)
    #print len(theList)

        if "call" in tokens :
            resp.say(output)#"Why are you texting me from %s" % sms.from_)
            client.calls.create(url="http://twimlets.com/echo?Twiml=" + urllib.quote_plus(str(resp)),
            to=sms.from_,
            from_=sms.to)
        elif end == "sonic" :
            resp.play(output)
            client.calls.create(url="http://twimlets.com/echo?Twiml=" + urllib.quote_plus(str(resp)),
            to=sms.from_,
            from_=sms.to)
    #elif end == "merchant":
        #apiKey = '190d85cd36b6a949a8828cc12e3892f5'
        #url = "http://api.reimaginebanking.com/merchants?key={}".foramt(apiKey)   
        #response = requests.get(url, headers={'content-type':'application/json'})
        elif end == "gif":
            accessTok="AtDBvC9A6iYdXiYrNRdCgp3zBmdHpr"
            giphy = json.loads(requests.get('http://api.giphy.com/v1/gifs/random?api_key=yoJC2lsdYpMXVbjZq8').text)
            clari = json.loads(requests.get("https://api.clarifai.com/v1/tag/?url="+giphy["data"]["image_url"]+"&access_token="+accessTok).text)
            theList.append({"p": sms.from_, "img": giphy["data"]["image_url"], "tags": clari["results"][0]["result"]["tag"]["classes"][0], "trys": 5})
            output = "We've got an image for you! Guess what one of it's tags are to see it :D (One is " + str(clari["results"][0]["result"]["tag"]["classes"][0][0]) + ")"
            resp.message(output)
        else :
            resp.message(output)#"Why are you texting me from %s" % sms.from_)

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)


