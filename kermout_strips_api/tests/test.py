#Install using pip first.
from kermout_strips_api import Plan

plan = {
    'Callsign': 'UAL256',
    'Aircraft': 'B737',
    'Flight_Rules': 'IFR',
    'Departure': 'KSAN',
    'Arrival': 'KJFK',
    'Altitude': '5000',
    'Routes': 'DCT GPS',
    'remarks': 'bout to go vertical',
}

s = Plan(plan)

s.filePlan()
s.startLoop()

inp = input("Stop?\n")
print("")

s.stopLoop()

s.deletePlan()