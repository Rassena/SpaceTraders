from data import api
from data.constants import *
from src.connection import *


def get_ships():
    return get_request(api.ships)


def get_ship(ship_id):
    return get_request(api.ship.format(ship_id))


def move_to(ship_id, waypoint_symbol):
    header = extend_header(H_CONTENT_TYPE_JSON)
    data = {WAYPOINT_SYMBOL: waypoint_symbol}
    return post_request(api.ship_navigate.format(ship_id), header=header, data=data)


def dock(ship_id):
    return post_request(api.ship_dock.format(ship_id))


def refuel(ship_id):
    return post_request(api.ship_refuel.format(ship_id))


def orbit(ship_id):
    return post_request(api.ship_orbit.format(ship_id))


def mine(ship_id):
    return post_request(api.ship_mine.format(ship_id))


def get_conteiner(ship_id):
    data = get_ship(ship_id)


def sell(ship_id, symbol, units):
    header = extend_header(H_CONTENT_TYPE_JSON)
    data = {
        SYMBOL: symbol,
        UNITS: units
    }
    return post_request(api.ship_sell.format(ship_id), header=header, data=data)
