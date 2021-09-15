from flask import Flask, request, jsonify
import json
from flask_pydantic_spec import (
    FlaskPydanticSpec,
    Response,
    Request
)
from entities.wallet import Wallet, WalletReport
from entities.investments import FixedRent, VariableRent
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware
from middleware import YAMLStorage, Encoder


server = Flask(__name__)
server.json_encoder = Encoder
spec = FlaskPydanticSpec('flask', title='MyInvestments')
spec.register(server)

database = TinyDB(filename='database.json', ensure_ascii=False, storage=YAMLStorage)



@server.get('/wallets')
# @spec.validate(resp=Response(HTTP_200=Wallet))
def get_wallet():
    with open('data.json', 'r') as data:
        response = json.load(data)
    return response

@server.get('/investments')
# @spec.validate(resp=Response(HTTP_200=VariableRent))
def all_investments():
    """
    Return all registers in database
    :return:
    """
    registers = jsonify(database.all())
    return registers




@server.post('/add_investment')
@spec.validate(body=Request(FixedRent), resp=Response(HTTP_200=WalletReport))
def add_investment():
    """
    Add and investment in wallet
    :return:
    """
    body = request.context.body.json()
    # body =
    database.insert(body)
    report = WalletReport(
        balance=500,
        profit=0.8,
        taxes=200 + body['amount']
    )
    return report.dict()


@server.post('/test')
@spec.validate(body=Request(VariableRent), resp=Response(HTTP_200=WalletReport))
def test():
    """
    Test database insertion
    :return:
    """
    body = request.context.body.dict()
    database.insert(body)
    report = WalletReport(
        balance=500,
        profit=0.8,
        taxes=200 + body['amount']
    ).dict()
    return report

@server.put('/investments/<string:title>')
@spec.validate(
    body=Request(VariableRent), resp=Response(HTTP_200=VariableRent)
)
def change_investment(title):
    VariableRent = Query()
    body = request.context.body.dict()
    database.update(body, VariableRent.title == title)
    return jsonify(body)

@server.delete('/investmets/<string:title>')
@spec.validate(resp=Response('HTTP_204'))
def delete_investment(title):
    VariableRent = Query()
    database.remove(VariableRent.title == title)
    return jsonify({})


server.run()
