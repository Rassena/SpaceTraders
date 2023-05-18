from time import sleep
from src.ships import *
from src.contract import *
from data.data import automation_data


transporter = automation_data.get("ships")[0]
miners = automation_data.get("ships")[1:]
contract_id = automation_data.get("contract_id")
wanted_resource = automation_data.get("wanted_resource")
destinationSymbol = automation_data.get("destinationSymbol")
mineral_source = automation_data.get("mineral_source")


def get_status(ship_data):
   return ship_data.get(DATA).get("nav").get("status")


def get_inventory(ship_id):
    sleep(1)
    return get_ship(ship_id).get(DATA).get("cargo").get("inventory")

def mine(miner):
    if not if_still_cooldown(miner):
        sleep(1)
        orbit(miner)
        sleep(1)
        return extract(miner)
    return None

def refuel_ship(ship_id):
    sleep(1)
    dock(ship_id)
    sleep(1)
    return refuel(ship_id)




def if_still_cooldown(ship_id):
    sleep(1)
    return get_cooldown(ship_id) != 204


def survey(transporter):
    sleep(1)
    ship_data = get_ship(transporter)
    if get_status(ship_data) in ['DOCKED','IN_ORBIT']:
        if ship_data.get(DATA).get("nav").get("destination").get("systemSymbol") == mineral_source:
            if not if_still_cooldown(transporter):
                sleep(1)
                orbit(transporter)
                response = create_survey(transporter)
                sleep(1)
                dock(transporter)
                print("survey created: {}".format(response.get(DATA).get(SURVEYS)))
                return True
    return False


def sell_unwanted(miner):
    sleep(1)
    dock(miner)
    inventory = get_inventory(miner)
    for unit in inventory:
        if unit.get(SYMBOL) != wanted_resource:
            sleep(1)
            response = sell(miner, unit.get(SYMBOL), unit.get(UNITS))
            transaction = response.get(DATA).get("transaction")
            print("{} --- sold {} {} for {} ".format(transaction.get("timestamp"),transaction.get("units"),transaction.get("tradeSymbol"),transaction.get("totalPrice")))


def get_wanted_units_from_cargo(cargo):
        for unit in cargo.get(""):
            if unit.get(SYMBOL) == wanted_resource:
                return unit.get(UNITS)
            

def get_free_space_from_cargo(cargo):
    return cargo.get("capacity") - cargo.get(UNITS)


def transfer_wanted_max(ship_id_1, ship_id_2):
    sleep(1)
    ship_id_1_wanted_units = get_wanted_units_from_cargo(get_cargo(ship_id_1).get(DATA))
    sleep(1)
    ship_id_2_cargo_free_space = get_free_space_from_cargo(get_cargo(ship_id_2).get(DATA))

    unit_to_transfer = min(ship_id_1_wanted_units,ship_id_2_cargo_free_space)
    if unit_to_transfer != 0:
        sleep(1)
        transfer_cargo(ship_id_1,ship_id_2,wanted_resource,unit_to_transfer)
    print("transfered from {} to {} {} {} ".format(ship_id_1,ship_id_2,unit_to_transfer,wanted_resource))



def transfer_wanted_to_transporter(miner):
    inventory = get_inventory(miner)
    available = False
    for unit in inventory:
            if unit.get(SYMBOL) == wanted_resource:
                available = True
    if available:
        sleep(1)
        miner_data = get_ship(miner) 
        sleep(1)
        transporter_data = get_ship(transporter)
        miner_pos = miner_data.get(DATA).get("nav").get("destination").get("systemSymbol")
        transporter_pos = transporter_data.get(DATA).get("nav").get("destination").get("systemSymbol")
        if miner_pos == transporter_pos:
            transfer_wanted_max(miner,transporter)


def loop():
    while True:

        #mining
        for miner in miners:
            response = mine(miner)
            if response:
                print("{} extracted: {} ; current cargo: {}".format(miner,response.get(DATA).get("extraction"),response.get(DATA).get("cargo")))
                print("{} refueled: {}".format(miner, refuel_ship(miner)))
                transfer_wanted_to_transporter(miner)
                sell_unwanted(miner)

        #transporter
        sleep(1)
        transporter_data = get_ship(transporter)
        if survey(transporter):
            transporter_cargo = transporter_data.get(DATA).get("cargo")
            free_space = get_free_space_from_cargo(transporter_data.get(DATA).get("cargo"))
            if free_space == 0:
                sleep(1)
                move_to(transporter,destinationSymbol)
                print("{} moved to {} ".format(transporter, destinationSymbol))
        elif transporter_data.get(DATA).get("nav").get("destination").get("systemSymbol") == destinationSymbol:
            if get_status(transporter_data) in ['DOCKED','IN_ORBIT']:
                print("{} refueled: {}".format(transporter, refuel_ship(transporter)))
                sleep(1)
                response = deliver_contract(transporter,contract_id,wanted_resource,get_wanted_units_from_cargo(transporter_cargo))
                print("delivery response: {}".format(response))
                sleep(1)
                move_to(transporter,mineral_source)





