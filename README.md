# DPW Simulation interacting with the territory in the DB

This specific branch from the repository, contains the code that simulates the behavior of the drones with the Directional Pheromone Walk algorithm, when they interact with the territory in a Neo4j database.

## Pre-requirements
- [Python 3](https://www.python.org/downloads/)
- [Requests](https://pypi.org/project/requests/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pygame](https://pypi.org/project/pygame/)

## Start the server

You must clone the [TFG-ComputerEngineering-API](https://github.com/moniwaterhouse/TFG-ComputerEngineering-API) and follow the instructions on its `README.md` file to start the server. This needs to be done prior to run this code since the simulation interacts with the Neo4j database throug that API.

## Start the simulation

To start the simulation, open a terminal in the root of the repository and run:

```shell
python3 ./main.py
```

You will see a window in which you will be able to select the `territory.txt` file, enter the number of drones and the pheromone intensity. Press the *Submit* button to start the simulation.

## Important notes

- Make sure that the `territory.txt` file contains the same amount of rows and columns to make sure that the elements are properly draw in the simulation window.
- Make sure that the `territory.txt` contains only 0 and 1. Otherwise, those characters will be interpreted as obstacles.
- The number of drones and the pheromone intensity should be integers.
- The recommended values for the number of drones are between 1 and 15.
- The recommended values for the pheromone intensity are between 100 and 500.

*** Note that bigger territories will require more computational resources so the simulation may take more time to complete, and you may see the drones moving slower.