import random

class Drone:

  def __init__(self, initialDirection, initialX, initialY, pheromoneIntensity):
    self.direction = initialDirection
    self.positionX = initialX
    self.positionY = initialY
    self.northValue = 0
    self.southValue = 0
    self.eastValue = 0
    self.westValue = 0
    self.northPheromone = 0
    self.southPheromone = 0
    self.eastPheromone = 0
    self.westPheromone = 0
    self.pheromoneIntensity = pheromoneIntensity
  
  def move(self, territory):
    moveOptions = self.getMoveOptions(territory)
    sortedOptions = sorted(moveOptions, key=lambda x: x[1])
    print("Sorted options: ", sortedOptions)
    print("Current direction: " + self.direction)
    options_number = len(sortedOptions)
    if options_number == 1:
      moveDirection = sortedOptions[0][0]
    elif options_number == 2:
      if sortedOptions[0][1] == sortedOptions[1][1]:
        position = random.randint(0, 1)
        moveDirection = sortedOptions[position][0]
      else:
        moveDirection = sortedOptions[0][0]
    elif options_number == 3:
      if sortedOptions[0][1] == sortedOptions[1][1]:
        if sortedOptions[0][1] == sortedOptions[2][1]:
          position = random.randint(0, 2)
          moveDirection = sortedOptions[position][0]
        else:
          position = random.randint(0, 1)
          moveDirection = sortedOptions[position][0]
      else:
        moveDirection = sortedOptions[0][0]
    print("Move direction: " + moveDirection)
    print("---------------------------------")
    self.changeCell(moveDirection)
    return

  def changeDirection(self, direction):
    cardinalPoints = ["north", "south", "east", "west"]
    cardinalPoints.remove(direction)
    directionIndex = random.randint(0,2)
    newDirection = cardinalPoints[directionIndex]
    self.direction = newDirection
    return newDirection

  def changeCell(self, moveDirection):
    if moveDirection == "north":
      self.positionY = self.positionY - 1
    elif moveDirection == "south":
      self.positionY = self.positionY + 1
    elif moveDirection == "east":
      self.positionX = self.positionX + 1
    elif moveDirection == "west":
      self.positionX = self.positionX - 1

  def getMoveOptions(self, territory):
    self.checkNeighborState(territory)
    moveOptions = []

    if self.eastValue == 0:
      moveOptions.append(("east", self.eastPheromone))
    if self.westValue == 0:
      moveOptions.append(("west", self.westPheromone))
    if self.northValue == 0:
      moveOptions.append(("north", self.northPheromone))
    if self.southValue == 0:
        moveOptions.append(("south", self.southPheromone))
  
    return moveOptions


  def checkNeighborState(self, territory):
    self.checkNorthNeighbor(territory)
    self.checkSouthNeighbor(territory)
    self.checkEastNeighbor(territory)
    self.checkWestNeighbor(territory)

  def checkNorthNeighbor(self, territory):
    if self.positionY == 0:
      self.northValue = 1
    else:
      self.northValue = territory[self.positionY-1][self.positionX].value
      self.northPheromone = territory[self.positionY-1][self.positionX].pheromoneIntensity
    return

  def checkSouthNeighbor(self, territory):
    if self.positionY == len(territory) - 1:
      self.southValue = 1
    else:
      self.southValue = territory[self.positionY+1][self.positionX].value
      self.southPheromone = territory[self.positionY+1][self.positionX].pheromoneIntensity
    return
  
  def checkEastNeighbor(self, territory):
    if self.positionX == len(territory)-1:
      self.eastValue = 1
    else:
      self.eastValue = territory[self.positionY][self.positionX+1].value
      self.eastPheromone = territory[self.positionY][self.positionX+1].pheromoneIntensity
    return
  
  def checkWestNeighbor(self, territory):
    if self.positionX == 0:
      self.westValue = 1
    else:
      self.westValue = territory[self.positionY][self.positionX-1].value
      self.westPheromone = territory[self.positionY][self.positionX-1].pheromoneIntensity
    return

  def depositPheromone(self, territory):
    territory[self.positionY][self.positionX].visited = "V"
    territory[self.positionY][self.positionX].pheromoneIntensity = self.pheromoneIntensity
    return territory