import logging
import sys
import time
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

'''
This file contains the code to test the autonomous flight of the Crazyflie 2.0 in a random trajectory
'''

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7') # Change this URI depending on your drone
TARGET_HEIGHT = 0.3 
TARGET_VELOCITY = 0.2
TRAVEL_DISTANCE = 0.2

deck_attached_event = Event()
logging.basicConfig(level=logging.ERROR)

'''
This method checks if the flow deck is properly attached to the Crazyflie
'''
def check_flow_deck(name, value_str):
    value = int(value_str)
    print(value)
    if value:
        deck_attached_event.set()
        print('Deck is attached!')
    else:
        print('Deck is NOT attached!')

'''
This method sets a random trajectory for the Crazyflie to follow
'''
def closed_trajectory(scf):
    with MotionCommander(scf, default_height=TARGET_HEIGHT) as mc:
        time.sleep(1)
        mc.forward(TRAVEL_DISTANCE, velocity=TARGET_VELOCITY)
        time.sleep(1)
        mc.right(TRAVEL_DISTANCE, velocity=TARGET_VELOCITY)
        time.sleep(1)
        mc.back(TRAVEL_DISTANCE, velocity=TARGET_VELOCITY)
        time.sleep(1)
        mc.left(TRAVEL_DISTANCE, velocity=TARGET_VELOCITY)

if __name__ == '__main__':

    # Initiates crazyflie drivers
    cflib.crtp.init_drivers()

    # Syncs with the Crazyflie
    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='cache')) as scf:
        
        # Checks if the flow deck is properly attached
        scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                         cb=check_flow_deck)
        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print('No flow deck detected!')
            sys.exit(1)

        closed_trajectory(scf)