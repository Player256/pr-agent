from flask import Flask,request,abort
import hmac
import json
import hashlib
import os
import requests

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
    payload = request.json
    response = requests.get(payload['pull_request']['diff_url'])
    print(response.text)
    return "Yay!"

if __name__ == '__main__':
    app.run(port = 5000)
