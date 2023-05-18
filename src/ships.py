from data import api
from data.constants import *
from src.connection import *
import data.data as data


def get_ship(ship_id):
    return get_request(api.ship.format(ship_id))


def move_to(ship_id, waypoint_symbol):
    header = extend_header(H_CONTENT_TYPE_JSON)
    data_to_send = {WAYPOINT_SYMBOL: waypoint_symbol}
    return post_request(api.ship_navigate.format(ship_id), header=header, data=data_to_send)


def dock(ship_id):
    return post_request(api.ship_dock.format(ship_id))


def refuel(ship_id):
    return post_request(api.ship_refuel.format(ship_id))


def orbit(ship_id):
    return post_request(api.ship_orbit.format(ship_id))


def extract(ship_id):
    return post_request(api.ship_extract.format(ship_id))


def get_cargo(ship_id):
    return get_request(api.ship_cargo.format(ship_id))


def create_survey(ship_id):
    header = extend_header(extend_header(H_ACCEPT, H_CONTENT_TYPE_JSON))
    response = post_request(api.ship_survey.format(ship_id), header)
    if response.get(DATA):
        data.surveys.extend(response.get(DATA).get(SURVEYS))
    else:
        # fixme: change to log
        print(response)
    return response


def scan_system(ship_id):
    header = extend_header(extend_header(H_ACCEPT, H_CONTENT_TYPE_JSON))
    return post_request(api.ship_scan_system.format(ship_id), header)


def get_cooldown(ship_id):
    return get_request(api.ship_get_cooldown.format(ship_id))


def sell(ship_id, symbol, units):
    header = extend_header(H_CONTENT_TYPE_JSON)
    data_to_send = {
        SYMBOL: symbol,
        UNITS: units
    }
    return post_request(api.ship_sell.format(ship_id), header=header, data=data_to_send)
