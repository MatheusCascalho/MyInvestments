from flask import Flask
import json
from flask_pydantic_spec import FlaskPydanticSpec

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='MyInvestments')
spec.register(server)


@server.get('/wallets')
def get_wallet():
    with open('data.json', 'r') as data:
        response = json.load(data)
    return response


server.run()
