from flask import Flask
import json

server = Flask(__name__)


@server.get('/wallets')
def get_wallet():
    with open('data.json', 'r') as data:
        response = json.load(data)
    return response


server.run()
