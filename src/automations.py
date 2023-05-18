from time import sleep
from src.ships import *


def sell_inventory(miner, inventory):
    dock(miner)
    for unit in inventory:
        print(sell(miner, unit.get(SYMBOL), unit.get(UNITS)))


def cargo_empty(cargo):
    capacity = cargo.get("capacity")
    units = cargo.get("units")
    inventory = cargo.get("inventory")


def miner_loop():
    miner_01 = "RASSENA-2"
    waypoint_01 = "X1-ZA40-99095A"
    current_contract = "clhrimv5d31cys60dq79ji82t"

    while True:
        cargo = get_ship(miner_01).get("data").get("cargo")
        sell_inventory(miner_01, cargo.get("inventory"))
        refuel(miner_01)
        orbit(miner_01)
        res = extract(miner_01)
        print(res)
        cooldown = res.get("data").get("cooldown").get("totalSeconds")
        print(f"sleep: {cooldown} sec")
        sleep(cooldown)
