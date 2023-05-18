import data.api as api
from connection import *
from data.constants import *


def get_contracts():
    return get_request(api.contracts)


def get_contract(contract_id):
    return get_request(api.contract.format(contract_id))


def deliver_contract(ship_id, contract_id, trade_symbol, unit):
    header = extend_header(extend_header(H_CONTENT_TYPE_JSON, H_ACCEPT))
    data_to_send = {
        SHIP_SYMBOL: ship_id,
        TRADE_SYMBOL: trade_symbol,
        UNITS: unit
    }
    return post_request(api.contract_deliver.format(contract_id), header=header, data=data_to_send)


def fulfill_contract(contract_id):
    header = extend_header(extend_header(H_CONTENT_TYPE_JSON, H_ACCEPT))
    return post_request(api.contract_fulfill.format(contract_id), header=header)
