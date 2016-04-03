from flask import Flask, request, redirect
import twilio.twiml
import json
import StringIO
import sys
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    txt = request.args.get('MessageSid', '')
    resp = twilio.twiml.Response()
    
    account_sid = "ACd56262f209cd94fe377106f857bd8f82"
    auth_token  = "2c0d255b6ad344bca74537fd5ca022c9"
    client = TwilioRestClient(account_sid, auth_token)
 
    sms = client.messages.get(txt)

    #print type(sms)
    #print sms.from_
    #numba = twilio.
    #tokens = txt.tokenize()
    
    #old_stdout = sys.stdout
    #mystdout = StringIO()
    #sys.stdout = mystdout

    #exec(sms.body)

    #sys.stdout = old_stdout

    #print mystdout
    #print mystdout.getvalue()
    #print type(exec(sms.body))
    

    #code = "print \"5\""
    with stdoutIO() as s:
        exec sms.body
        #exec code

    print sms.body
    print s.getvalue()
    #resp.message(ret)
    #resp.message(mystdout.getvalue())
    resp.message("Why are you texting me from %s" % sms.from_)# % sms.from)
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)

