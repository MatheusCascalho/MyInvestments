from flask import Flask
import json
from flask_pydantic_spec import FlaskPydanticSpec, Response
from entities.wallet import Wallet

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='MyInvestments')
spec.register(server)


@server.get('/wallets')
@spec.validate(resp=Response(HTTP_200=Wallet))
def get_wallet():
    with open('data.json', 'r') as data:
        response = json.load(data)
    return response


server.run()
