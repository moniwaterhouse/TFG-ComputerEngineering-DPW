import pygame
from Territory.territory import Territory
from Drone.drone import Drone
from client.dpw_client import check_if_visited, check_current_type, evaporate_pheromones, check_current_pheromone, deposit_pheromone
from client.territory_client import initiate_territory, delete_territory, check_exploration

WIDTH, HEIGHT = 600, 600
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) 
start = True

'''
This method gets the dimensions of the territory.
'''          
def get_territory_dimensions(territory_path):
    try:
        with open(territory_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File '{territory_path}' not found.")
        return -1

''' 
This method sets the cell size according to the dimensions of the territory. This helps to fit the territory inside
the simulation window.
'''
def set_cell_size(territory_path):
    lines_count = get_territory_dimensions(territory_path)
    cell_size = WIDTH/lines_count
    return cell_size

''' 
This method draws the territory in the simulation. It draws squares of different colors depending on the type of 
cell and the pheromone intensity in the free cells. It checks the type of cells and the pheromone intensity in the DB
using the requests from the client.
'''    
def draw_territory(width, length, cell_size, WIN):
    for i in range(0, length):
        for j in range(0, width):
            pheromone_intensity = check_current_pheromone(j,i)
            cell_type = check_current_type(j,i)
            if cell_type == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*cell_size,i*cell_size,cell_size, cell_size),0)
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
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*cell_size,i*cell_size,cell_size, cell_size),0)

'''
This method is used to draw the drones in the simulation
'''
def draw_drone(pos_x, pos_y, cell_size, WIN):
    # Draw a circle
    circle_center_x = pos_x * cell_size + cell_size // 2
    circle_center_y = pos_y * cell_size + cell_size // 2
    circle_radius = cell_size // 4
    pygame.draw.circle(WIN, DRONE_COLOR, (circle_center_x, circle_center_y), circle_radius, 0)

'''
This method is used to start the simulation. It contains all the logic to create the territory,
for the drone to interact with the territory in DB, to draw all the elements on the simulation and to stop the simulation
when there are no missing cells left to explore. 
'''
def start_simulation(territory_path, drone_number, pheromone_intensity):
    
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Directional Pheromone Walk Simulation")

    territory_path = territory_path
    print(territory_path)
    cell_size = set_cell_size(territory_path)

    delete_territory() # Deletes the territory in case 
    initiate_territory(territory_path)
    run = True
    clock = pygame.time.Clock()

    new_territory = Territory(territory_path)
    territory_width = new_territory.num_cols
    territory_length = new_territory.num_rows
    drones = []

    #Creates one instance of each of the drones, so they can make their decisions independently 
    for i in range(1, drone_number + 1):
        if i%4 == 0:
            drone = Drone("north",0,0,pheromone_intensity)
        elif i%3 == 0:
            drone = Drone("south",0,0,pheromone_intensity)
        elif i%2 == 0:
            drone = Drone("east",0,0,pheromone_intensity)
        else:
            drone = Drone("west",0,0,pheromone_intensity)
        drones.append(drone)

    missingCells = True
    print_statistics = False
    counter = 0

    # Each drone deposits a pheromone in the initial cell
    for drone in drones:
        deposit_pheromone(drone.pos_x, drone.pos_y, pheromone_intensity)

    while run:
        clock.tick(200)
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        '''
        If there are missing cells, it runs an interaction of the DPW algorithm, where the drone interacts 
        with the territory, moves to the chosen cell and it shows on the simulation the changes.
        '''
        if missingCells:
            draw_territory(territory_width, territory_length, cell_size, WIN)
            for drone in drones:
                draw_drone(drone.pos_x, drone.pos_y, cell_size, WIN)
                move = drone.move()
            pygame.display.update()
            counter = counter + 1
            evaporate_pheromones()
            missingCells = check_exploration()
            if not missingCells:
                print_statistics = True
                
        # This is the condition to stop the simulation
        elif print_statistics:
            draw_territory(territory_width, territory_length, cell_size, WIN)
            for drone in drones:
                draw_drone(drone.pos_x, drone.pos_y, cell_size, WIN)
            pygame.display.update()
            counter = counter + 1
            for drone in drones:
                move = drone.move()
            evaporate_pheromones()
            print_statistics = False

    pygame.quit()
    