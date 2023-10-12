import pygame
import time
from client.config import Config
from Territory.territory import Territory
from Drone.drone import Drone
from client.dpw_client import check_if_visited, check_current_type, evaporate_pheromones, deposit_pheromone, check_east_neighbor, check_east_pheromone, check_north_neighbor, check_north_pheromone, check_south_neighbor, check_south_pheromone, check_west_neighbor, check_west_pheromone, check_current_pheromone


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 120
DRONE_NUMBER = 1
PHEROMONE_INTENSITY = 500
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
WHITE = (255, 255, 255)
TERRITORY_PATH = "Territory/territory.txt"

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")


def draw_territory(territory, width, length):
    for i in range(0, length):
        for j in range(0, width):
            pheromone_intensity = check_current_pheromone(i,j)
            cell_type = check_current_type(i,j)
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
                    is_visited = check_if_visited(i,j)
                    if(is_visited == "F"):
                        pheromoneColor = WHITE
                    else:
                        pheromoneColor = (76, 229, 229)
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def draw_drone(pos_x, pos_y):
    pygame.draw.rect(WIN, DRONE_COLOR, pygame.Rect(pos_x*CELL_SIZE,pos_y*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def main():
    run = True
    clock = pygame.time.Clock()

    new_territory = Territory(TERRITORY_PATH)
    territory = new_territory.matrix
    territory_width = new_territory.num_cols
    territory_length = new_territory.num_rows

    drones = []

    '''for i in range(1, DRONE_NUMBER + 1):
        if i%4 == 0:
            drone = Drone("north",0,0,PHEROMONE_INTENSITY)
        elif i%3 == 0:
            drone = Drone("south",0,0,PHEROMONE_INTENSITY)
        elif i%2 == 0:
            drone = Drone("east",0,0,PHEROMONE_INTENSITY)
        else:
            drone = Drone("west",0,0,PHEROMONE_INTENSITY)
        drones.append(drone)'''

    drone = Drone("south",0,0,PHEROMONE_INTENSITY)
    drones.append(drone)

    missingCells = True
    counter = 0
    territory = drone.depositPheromone(territory)

    while run:
        clock.tick(200)
        WIN.fill((255,255,255))
        
        draw_territory(territory, territory_width, territory_length)
        for drone in drones:
            draw_drone(drone.positionX, drone.positionY)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if missingCells:
            counter = counter + 1
            missingCells = False
            for drone in drones:
                drone.move(territory)
                territory = drone.depositPheromone(territory)
            for row in territory:
                for cell in row:
                    cell.evaporatePheromone()
                    if cell.visited == "F":
                        missingCells = True
        else:
            print("Iterations: ", counter)
        
        time.sleep(2.0)
    
    pygame.quit()

main()