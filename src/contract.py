from data import api
from src.connection import *


def get_contracts():
    return get_request(api.contracts)


def get_contract(contract_id):
    return get_request(api.contract.format(contract_id))
