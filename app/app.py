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

# Databases
database = TinyDB(filename='database.json', ensure_ascii=False, storage=YAMLStorage)
variable_rents_db = TinyDB('variable_rents_db.json', ensure_ascii=False, storage=YAMLStorage)
fixed_rents_db = TinyDB('fixed_rents_db.json', ensure_ascii=False, storage=YAMLStorage)
wallets_db = TinyDB('wallets_db.json', ensure_ascii=False, storage=YAMLStorage)


@server.get('/dummy_report')
# @spec.validate(resp=Response(HTTP_200=Wallet))
def get_wallet():
    with open('wallet_report_V0.json', 'r') as file:
        data = json.load(file)
    return data


@server.get('/dummy_report')
# @spec.validate(resp=Response(HTTP_200=Wallet))
def get_wallet():
    with open('wallet_report_V0.json', 'r') as file:
        data = json.load(file)
    return data

server.run()
