from flask import Flask,request
from websocket import connectServer
import re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Winja CTF!!!'

@app.route('/websocket')
def websocket():
    domain = request.args.get('domain')
    port = request.args.get('port')
    pattern = r"[^a-zA-Z0-9\.]"
    try:
        port = int(port)
        url = re.sub(pattern,'',domain)
        if not url:
            raise Exception("Something wrong in the domain")
    except Exception:
        return "Wrong domain name or port"

    try:
        connectServer(url, port)
    except Exception:
        return "Request Failed..."
    return "Request Sent Successfully..."

