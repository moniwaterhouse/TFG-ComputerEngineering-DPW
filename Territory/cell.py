''' 
This class represents a cell of the territory. It is used for simulation purposes to draw the cells in the pygame window.
'''
class Cell:

  def __init__(self, value):
    # If value = 0 is an empty space, if it is not 0 then is an obstacle
    self.value = value
    self.pheromoneIntensity = 0
    if self.value == 0:
      self.visited = "F"
    else:
      self.visited = "-"
