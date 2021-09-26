from flask import Flask, request, jsonify
import json
from flask_pydantic_spec import (
    FlaskPydanticSpec,
    Response,
    Request
)
from entities.wallet import Wallet, WalletReport
from entities.investments import FixedRent, VariableRent, VariableRentTypes, Sectors
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware
from middleware import YAMLStorage, Encoder
from typing import List


server = Flask(__name__)
server.json_encoder = Encoder
spec = FlaskPydanticSpec('flask', title='MyInvestments')
spec.register(server)

database = TinyDB(filename='database.json', ensure_ascii=False, storage=YAMLStorage)
variable_rents_db = TinyDB('variable_rents_db.json', ensure_ascii=False, storage=YAMLStorage)
fixed_rents_db = TinyDB('fixed_rents_db.json', ensure_ascii=False, storage=YAMLStorage)
wallets_db = TinyDB('wallets_db.json', ensure_ascii=False, storage=YAMLStorage)


@server.post('/add_variable_rent')
@spec.validate(body=Request(VariableRent))
def add_variable_rend():
    """
    Add and investment in wallet
    :return:
    """
    body = request.context.body.dict()
    # body =
    variable_rents_db.insert(body)

    return {"message": "Investment successfully added"}


@server.post('/add_fixed_rent')
@spec.validate(body=Request(FixedRent))
def add_fixed_rent():
    """
    Add and investment in wallet
    :return:
    """
    body = request.context.body.dict()
    # body =
    fixed_rents_db.insert(body)

    return {"message": "Investment successfully added"}


@server.get('/wallets')
# @spec.validate(resp=Response(HTTP_200=Wallet))
def get_wallet():
    from_database = jsonify(wallets_db.all()).json[0]
    wallet = Wallet.parse_obj(from_database)
    wallet.update_investment_values()
    encoder = Encoder()
    response = encoder.decode_dictionaries(wallet.dict())
    return response


@server.get('/investments')
# @spec.validate(resp=Response(HTTP_200=VariableRent))
def all_investments():
    """
    Return all registers in database
    :return:
    """
    variable_rents = jsonify(variable_rents_db.all())
    fixed_rents = jsonify(fixed_rents_db.all())
    registers = {
        "fixed_rent": fixed_rents.json,
        "variable_rents": variable_rents.json
    }

    return registers


@server.post('/add_investment')
@spec.validate(body=Request(FixedRent), resp=Response(HTTP_200=WalletReport))
def add_investment():
    """
    Add and investment in wallet
    :return:
    """
    body = request.context.body.dict()
    # body =
    database.insert(body)
    report = WalletReport(
        balance=500,
        profit=0.8,
        taxes=200 + body['amount']
    )
    return report.dict()


@server.post('/add_wallet')
@spec.validate(body=Request(Wallet))
def add_wallet():
    """
    Add and investment in wallet
    :return:
    """
    body: Wallet = Wallet.parse_obj(request.context.body.dict())
    body.fixed_rents = fixed_rents_db.all()
    body.variable_rents = variable_rents_db.all()

    encoder = Encoder()
    body = encoder.decode_dictionaries(body.dict())
    # body
    wallets_db.insert(body)

    return Wallet.parse_obj(body)



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

if __name__ == "__main__":
    ...
    # investments = variable_rents_db.all()
    # for investment in investments:
    #     investment['type'] = VariableRentTypes[investment['type'].upper()]
    #     investment['sector'] = Sectors[investment['sector'].upper()]
    # investments: List[VariableRent] = [VariableRent.parse_obj(data) for data in investments]
    # for investment in investments:
    #     investment.update_history()
    # print(investments[0])