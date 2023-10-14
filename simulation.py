import pygame
import time
from client.config import Config
from Territory.territory import Territory
from Drone.drone import Drone
from client.dpw_client import check_if_visited, check_current_type, evaporate_pheromones, check_current_pheromone, deposit_pheromone
from client.territory_client import initiate_territory, delete_territory, check_exploration

import logging
import sys
import time
from threading import Event
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 120
DRONE_NUMBER = 1
PHEROMONE_INTENSITY = 500
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
WHITE = (255, 255, 255)
TERRITORY_PATH = "Territory/territory.txt"

URI = Config.URI
TARGET_ALT = Config.TARGET_ALT

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

deck_attached_event = Event()
logging.basicConfig(level=logging.ERROR)

def param_deck_flow(name, value_str):
    value = int(value_str)
    print(value)
    if value:
        deck_attached_event.set()
        print('Deck is attached!')
    else:
        print('Deck is NOT attached!')


def draw_territory(width, length):
    for i in range(0, length):
        for j in range(0, width):
            pheromone_intensity = check_current_pheromone(j,i)
            cell_type = check_current_type(j,i)
            if cell_type == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)
            else:
                if pheromone_intensity in range(337, 501):
                    pheromoneColor = (229, 66 + (500 - pheromone_intensity), 66)
                elif pheromone_intensity in range(174, 337):
                    pheromoneColor = (pheromone_intensity - 109, 229, 66)
                elif pheromone_intensity in range(11, 174):
                    pheromoneColor = (66, 229, 66 + (173 - pheromone_intensity))
                elif pheromone_intensity in range (1, 11):
                    pheromoneColor = (66 + (10 - pheromone_intensity), 229, 229)
                else:
                    is_visited = check_if_visited(j,i)
                    if(is_visited == "F"):
                        pheromoneColor = WHITE
                    else:
                        pheromoneColor = (76, 229, 229)
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def draw_drone(pos_x, pos_y):
    # Draw a circle
    circle_center_x = pos_x * CELL_SIZE + CELL_SIZE // 2
    circle_center_y = pos_y * CELL_SIZE + CELL_SIZE // 2
    circle_radius = CELL_SIZE // 4
    pygame.draw.circle(WIN, DRONE_COLOR, (circle_center_x, circle_center_y), circle_radius, 0)

def main():
    delete_territory()
    initiate_territory("/Users/moniwaterhouse/TFG-ComputerEngineering-DPW/Territory/territory.txt")
    run = True
    clock = pygame.time.Clock()

    cflib.crtp.init_drivers()

    new_territory = Territory(TERRITORY_PATH)
    territory_width = new_territory.num_cols
    territory_length = new_territory.num_rows
    initial_coordinate = (0,0,Config.TARGET_ALT, 0)
    coordinates = []
    coordinates.append(initial_coordinate)
    drones = []

    for i in range(1, DRONE_NUMBER + 1):
        if i%4 == 0:
            drone = Drone("north",0,0,PHEROMONE_INTENSITY)
        elif i%3 == 0:
            drone = Drone("south",0,0,PHEROMONE_INTENSITY)
        elif i%2 == 0:
            drone = Drone("east",0,0,PHEROMONE_INTENSITY)
        else:
            drone = Drone("west",0,0,PHEROMONE_INTENSITY)
        drones.append(drone)

    missingCells = True
    print_statistics = False
    counter = 0
    for drone in drones:
        deposit_pheromone(drone.pos_x, drone.pos_y, Config.PHEROMONE_INTENSITY)
    

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='/Users/moniwaterhouse/TFG-ComputerEngineering-DPW/cache')) as scf:

        scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                         cb=param_deck_flow)
        time.sleep(1)

        if not deck_attached_event.wait(timeout=5):
            print('No flow deck detected!')
            run = False
            sys.exit(1)
            
        with MotionCommander(scf, default_height=TARGET_ALT) as mc:
            time.sleep(1.0)
            while run:
                clock.tick(200)
                WIN.fill((255,255,255))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                
                if missingCells:
                    counter = counter + 1
                    for drone in drones:
                        drone.move(mc)
                    evaporate_pheromones()
                    missingCells = check_exploration()
                    
                    draw_territory(territory_width, territory_length)
                    for drone in drones:
                        draw_drone(drone.pos_x, drone.pos_y)
                    pygame.display.update()

                    if not missingCells:
                        print_statistics = True
                
                elif print_statistics:
                    draw_territory(territory_width, territory_length)
                    for drone in drones:
                        draw_drone(drone.pos_x, drone.pos_y)
                    pygame.display.update()
                    counter = counter + 1
                    for drone in drones:
                        drone.move(mc)
                    evaporate_pheromones()
                    print("Iterations: ", counter)
                    print("Coordinates: ")
                    for coord in coordinates:
                        print(coord)
                    print_statistics = False
                    
                else:
                    time.sleep(5.0)
                
                
                time.sleep(1.0)
            
            pygame.quit()
        


main()