import pygame
from client.config import Config
from Territory.territory import Territory
from Drone.drone import Drone
from client.dpw_client import check_if_visited, check_current_type, evaporate_pheromones, check_current_pheromone, deposit_pheromone
from client.territory_client import initiate_territory, delete_territory, check_exploration
import pygame_menu as pm 

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 120
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) 
start = True

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def enter_parameters():
    drones_number = [("1", 1),
				  ("2", 2),
				  ("3", 3),
				  ("4", 4),
				  ("5", 5),
				  ("6", 6),
				  ("7", 7),
				  ("8", 8),
				  ("9", 9),
				  ("10", 10)]
    
    altitude = [("0.5", 0.5),
             ("0.2", 0.2),
			 ("0.3", 0.3),
			 ("0.4", 0.4),
			 ("0.6", 0.6),
			 ("0.7", 0.7),
			 ("0.8", 0.8),
			 ("0.9", 0.9),
			 ("1.0", 1.0)]
    
    pheromone_intensity = [("100", 100),
						("200", 200),
						("300", 300),
						("400", 400),
						("500", 500)]
    
    travel_distance = [
					("0.2", 0.2),
                    ("0.1", 0.1),
					("0.3", 0.3),
					("0.4", 0.4),
					("0.5", 0.5),
					("0.6", 0.6),
					("0.7", 0.7),
					("0.8", 0.8),
					("0.9", 0.9),
					("1.0", 1.0)]

    speed = [
					("0.2", 0.2),
                    ("0.1", 0.1),
					("0.3", 0.3),
					("0.4", 0.4),
					("0.5", 0.5),
					("0.6", 0.6),
					("0.7", 0.7),
					("0.8", 0.8),
					("0.9", 0.9),
					("1.0", 1.0)]
    
    def start_simulation_action():

        start_window_data = start_window.get_input_data() 

        Config.DRONE_NUMBER = start_window_data.get("drones_number")[0][1]
        Config.TARGET_ALT = start_window_data.get("altitude")[0][1]
        Config.TRAVEL_DISTANCE = start_window_data.get("travel_distance")[0][1]
        Config.PHEROMONE_INTENSITY = start_window_data.get("pheromone_intensity")[0][1]
        Config.SPEED = start_window_data.get("speed")[0][1]
    
        delete_territory()
        initiate_territory("/Users/moniwaterhouse/TFG-ComputerEngineering-DPW/Territory/territory.txt")
        run = True
        clock = pygame.time.Clock()

        new_territory = Territory(Config.TERRITORY_PATH)
        territory_width = new_territory.num_cols
        territory_length = new_territory.num_rows
        movements = []
        drones = []

        for i in range(1, Config.DRONE_NUMBER + 1):
            if i%4 == 0:
                drone = Drone("north",0,0,Config.PHEROMONE_INTENSITY)
            elif i%3 == 0:
                drone = Drone("south",0,0,Config.PHEROMONE_INTENSITY)
            elif i%2 == 0:
                drone = Drone("east",0,0,Config.PHEROMONE_INTENSITY)
            else:
                drone = Drone("west",0,0,Config.PHEROMONE_INTENSITY)
            drones.append(drone)

        missingCells = True
        print_statistics = False
        counter = 0
        for drone in drones:
            deposit_pheromone(drone.pos_x, drone.pos_y, Config.PHEROMONE_INTENSITY)
        


        while run:
            clock.tick(200)
            WIN.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            if missingCells:
                draw_territory(territory_width, territory_length)
                for drone in drones:
                    draw_drone(drone.pos_x, drone.pos_y)
                    move = drone.move()
                    movements.append(move)
                pygame.display.update()
                counter = counter + 1
                evaporate_pheromones()
                missingCells = check_exploration()
                if not missingCells:
                    print_statistics = True
                
            
            elif print_statistics:
                draw_territory(territory_width, territory_length)
                for drone in drones:
                    draw_drone(drone.pos_x, drone.pos_y)
                pygame.display.update()
                counter = counter + 1
                for drone in drones:
                    move = drone.move()
                movements.append(move)
                evaporate_pheromones()
                print("Iterations: ", counter)
                print("Movements: ")
                print(movements)
                print_statistics = False
            

    def printSettings(): 
        print("\n\n") 
		# getting the data using "get_input_data" method of the Menu class 
        start_window_data = start_window.get_input_data() 

        for key in start_window_data.keys(): 
            print(f"{key}\t:\t{start_window_data[key]}")
	
	# Creating the settings menu 
    start_window = pm.Menu(title="Crazyflie 2.0 - DPW Parameters", 
					width=WIDTH, 
					height=HEIGHT, 
					theme=pm.themes.THEME_BLUE) 
	
	# Adjusting the default values 
    start_window._theme.widget_font_size = 25
    start_window._theme.widget_font_color = BLACK 

	# 2 different Drop-downs to select the graphics level and the resolution level 
    start_window.add.dropselect(title="Number of drones", items=drones_number, 
							dropselect_id="drones_number", default=0)
    start_window.add.dropselect(title="Altitude (m)", items=altitude, 
							dropselect_id="altitude", default=0)
    start_window.add.dropselect(title="Pheromone intensity", items=pheromone_intensity, 
							dropselect_id="pheromone_intensity", default=0)
    start_window.add.dropselect(title="Travel distance (m)", items=travel_distance, 
							dropselect_id="travel_distance", default=0)
    start_window.add.dropselect(title="Speed (m/s)", items=speed, 
							dropselect_id="speed", default=0)
    
    start_window.add.button(title="Start", action=start_simulation_action, 
                        font_color=WHITE, background_color=GREEN) 
	
	# Lets us loop the main menu on the screen 
    start_window.mainloop(WIN) 

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

    enter_parameters()
    
    pygame.quit()
    


main()