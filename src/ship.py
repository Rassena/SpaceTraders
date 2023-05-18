from data import api
from data.constants import *
from src.connection import *
from datetime import datetime


def get_ships():
    return get_request(api.ships)


class Ship:

    def __init__(self, name):
        self.data = None
        self.name = name
        self.update_ship()

    def update_ship(self):
        self.data = get_request(api.ship.format(self.name)).get(DATA)

    def move_to(self, waypoint_symbol):
        header = extend_header(H_CONTENT_TYPE_JSON)
        data = {WAYPOINT_SYMBOL: waypoint_symbol}
        post_request(api.ship_navigate.format(self.name), header=header, data=data)

    def dock(self):
        self.data.update(post_request(api.ship_dock.format(self.name)).get(DATA))

    def refuel(self):
        post_request(api.ship_refuel.format(self.name))

    def orbit(self):
        self.data.update(post_request(api.ship_orbit.format(self.name)))

    def mine(self):
        post_request(api.ship_mine.format(self.name))

    def get_container(self):
        return self.data.get(CONTAINER)

    def sell(self, symbol, units):
        header = extend_header(H_CONTENT_TYPE_JSON)
        data = {
            SYMBOL: symbol,
            UNITS: units
        }
        return post_request(api.ship_sell.format(self.name), header=header, data=data)
