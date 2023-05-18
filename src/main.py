from time import sleep

from contract import *
from ships import *


def can_mine(miner):
    pass


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


if __name__ == "__main__":
    # print(get_contract(current_contract))
    # print(get_ship(miner_01))
    # print(move_to(miner_01, waypoint_01))
    # print(dock(miner_01))
    # print(refuel(miner_01))

    miner_01 = "RASSENA-2"
    main_ship = "RASSENA-1"

    # print(mine(miner_01))
    # data: dict = get_ship(miner_01)

    # cargo = data.get("data").get("cargo")
    # capacity = cargo.get("capacity")
    # units = cargo.get("units")
    # inventory = cargo.get("inventory")

    # print(sell(miner_01, "ALUMINUM_ORE", 8))

    # miner_loop()

    create_survey(main_ship)
