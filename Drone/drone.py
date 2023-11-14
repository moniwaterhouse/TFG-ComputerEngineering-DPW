import random
from client.dpw_client import deposit_pheromone, check_east_neighbor, check_north_neighbor, check_south_neighbor, check_west_neighbor, check_north_pheromone, check_south_pheromone, check_east_pheromone, check_west_pheromone

''' 
This class represents the drone and the actions it has to do to perform all the require steps to decide to which cell 
it should move based in the DPW algorithm.
'''
class Drone:

  def __init__(self, initial_direction, initial_x, initial_y, pheromone_intensity):
    self.direction = initial_direction
    self.pos_x= initial_x
    self.pos_y = initial_y
    self.north_value = 0
    self.south_value = 0
    self.east_value = 0
    self.west_value = 0
    self.north_pheromone = 0
    self.south_pheromone = 0
    self.east_pheromone = 0
    self.west_pheromone = 0
    self.pheromone_intensity = pheromone_intensity
  
  '''
  This method, gets the move options and sort them according their pheromone intensity. It choses the cell which has 
  the lowest pheromone intensity, and if there are two or more cells with the same pheromone intensity, it choses one 
  randomly. 
  '''
  def move(self):
    move_options = self.get_move_options()
    sorted_options = sorted(move_options, key=lambda x: x[1])

    options_number = len(sorted_options)

    if options_number == 1:
      move_direction = sorted_options[0][0]
    elif options_number == 2:
      if sorted_options[0][1] == sorted_options[1][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0]])
      else:
        move_direction = sorted_options[0][0]
    elif options_number == 3:
      if sorted_options[0][1] == sorted_options[1][1] == sorted_options[2][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0], sorted_options[2][0]])
      elif sorted_options[0][1] == sorted_options[1][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0]])
      else:
        move_direction = sorted_options[0][0]
    else:
      if sorted_options[0][1] == sorted_options[1][1] == sorted_options[2][1] == sorted_options[3][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0], sorted_options[2][0, sorted_options[3][1]]])
      elif sorted_options[0][1] == sorted_options[1][1] == sorted_options[2][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0], sorted_options[2][0]])
      elif sorted_options[0][1] == sorted_options[1][1]:
        move_direction = random.choice([sorted_options[0][0], sorted_options[1][0]])
      else:
        move_direction = sorted_options[0][0]

    self.change_cell(move_direction)
    deposit_pheromone(self.pos_x, self.pos_y, self.pheromone_intensity)
    return move_direction

  '''This method changes the direction of the drone if there is an obstacle in the current direction'''
  def change_direction(self, direction):
    cardinal_points = ["north", "south", "east", "west"]
    cardinal_points.remove(direction)
    direction_index = random.randint(0,2)
    new_direction = cardinal_points[direction_index]
    self.direction = new_direction
    return new_direction

  '''This method changes the position of the drone depending on the direction that is received as parameter'''
  def change_cell(self, move_direction):
    if move_direction == "north":
      self.pos_y = self.pos_y - 1
    elif move_direction == "south":
      self.pos_y = self.pos_y + 1
    elif move_direction == "east":
      self.pos_x = self.pos_x + 1
    elif move_direction == "west":
      self.pos_x = self.pos_x - 1
    return

  ''' 
  This method checks all neighbors (without considering the direction), to determine wether they are obstacles or free 
  cells. If a cell is free of obstacles, it is added to the move_options list as a tuple with the form 
  (direction, pheromone_intensity).
  '''
  def get_move_options(self):

    self.check_neighbors_state()
    move_options = []

    if self.north_value == 0:
      move_options.append(("north", self.north_pheromone))
    if self.south_value == 0:
      move_options.append(("south", self.south_pheromone))
    if self.east_value == 0:
      move_options.append(("east", self.east_pheromone))
    if self.west_value == 0:
      move_options.append(("west", self.west_pheromone))
  
    return move_options

  ''' 
  This method checks all neighbors, except the neighbor in the opposite of the predefined direction, to determine wether they are obstacles or free 
  cells. If a cell is free of obstacles, it is added to the move_options list as a tuple with the form 
  (direction, pheromone_intensity).
  '''
  def get_move_options_directional(self):
    self.check_neighbors_state()
    move_options = []
    if self.direction == "north":      
      if self.east_value == 0:
        move_options.append(("east", self.east_pheromone))
      if self.west_value == 0:
        move_options.append(("west", self.west_pheromone))
      if self.north_value == 0:
       move_options.append(("north", self.north_pheromone))
      else:
        if len(move_options) == 0:
          self.direction = "south"
          move_options.append(("south", self.south_pheromone))
        else:
          self.change_direction("north")

    elif self.direction == "south":
      if self.eastValue == 0:
        move_options.append(("east", self.east_pheromone))
      if self.westValue == 0:
        move_options.append(("west", self.west_pheromone))
      if self.southValue == 0:
        move_options.append(("south", self.south_pheromone))
      else:
        if len(move_options) == 0:
          self.direction = "north"
          move_options.append(("north", self.south_pheromone))
        else:
          self.change_direction("south")

    elif self.direction == "east":
      if self.north_value == 0:
        move_options.append(("north", self.north_pheromone))
      if self.south_value == 0:
        move_options.append(("south", self.south_pheromone))
      if self.east_value == 0:
        move_options.append(("east", self.east_pheromone))
      else:
        if len(move_options) == 0:
          self.direction = "west"
          move_options.append(("west", self.south_pheromone))
        else:
          self.change_direction("east")

    elif self.direction == "west":
      if self.north_value == 0:
        move_options.append(("north", self.north_pheromone))
      if self.south_value == 0:
        move_options.append(("south", self.south_pheromone))
      if self.west_value == 0:
        move_options.append(("west", self.west_pheromone))
      else:
        if len(move_options) == 0:
          self.direction = "east"
          move_options.append(("east", self.south_pheromone))
        else:
          self.change_direction("west")
    return move_options

  '''
  This methods gets the type and the pheromone intensity of all adjacent neighbors of the cell where the drone is positioned
  '''
  def check_neighbors_state(self):
    self.north_value = check_north_neighbor(self.pos_x, self.pos_y)
    self.north_pheromone = check_north_pheromone(self.pos_x, self.pos_y)

    self.south_value = check_south_neighbor(self.pos_x, self.pos_y)
    self.south_pheromone = check_south_pheromone(self.pos_x, self.pos_y)

    self.east_value = check_east_neighbor(self.pos_x, self.pos_y)
    self.east_pheromone = check_east_pheromone(self.pos_x, self.pos_y)

    self.west_value = check_west_neighbor(self.pos_x, self.pos_y)
    self.west_pheromone = check_west_pheromone(self.pos_x, self.pos_y)

    return

  