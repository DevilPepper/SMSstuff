from flask import Flask, request, redirect
import twilio.twiml
import json
from lxml import etree
import StringIO
import sys
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import contextlib
import urllib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #"""Respond to incoming calls with a simple text message."""
 
    txt = request.args.get('MessageSid', '')
    resp = twilio.twiml.Response()
    
    account_sid = "ACd56262f209cd94fe377106f857bd8f82"
    auth_token  = "2c0d255b6ad344bca74537fd5ca022c9"
    client = TwilioRestClient(account_sid, auth_token)
 
    sms = client.messages.get(txt)

    #print sms.from_
    tokens = sms.body.split()
    


    print sms.body
    
    if "call" in tokens :
        resp.say("Why are you texting me from %s" % sms.from_)
        client.calls.create(url="http://twimlets.com/echo?Twiml=" + urllib.quote_plus(str(resp)),
        to=sms.from_,
        from_=sms.to)
    else :
        resp.message("Why are you texting me from %s" % sms.from_)

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)


