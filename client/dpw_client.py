import requests
from client.config import Config

'''This file contains all the client requests that can be made to the server to interact with the territory in the DB'''
base_url = Config.BASE_URL

# Request to deposit pheromone in a cell
def deposit_pheromone(x_pos, y_pos, pheromone_intensity):
    url = f'{base_url}/dpw/deposit-pheromone/{x_pos}/{y_pos}/{pheromone_intensity}'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Request to evaporate all pheromones
def evaporate_pheromones():
    url = f'{base_url}/dpw/evaporate-pheromones'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Request to check north neighbor's type
def check_north_neighbor(x_pos, y_pos):
    url = f'{base_url}/dpw/check-north-neighbor/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("North neighbor type: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check south neighbor's type
def check_south_neighbor(x_pos, y_pos):
    url = f'{base_url}/dpw/check-south-neighbor/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("South neighbor type: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check east neighbor's type
def check_east_neighbor(x_pos, y_pos):
    url = f'{base_url}/dpw/check-east-neighbor/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("East neighbor type: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check west neighbor's type
def check_west_neighbor(x_pos, y_pos):
    url = f'{base_url}/dpw/check-west-neighbor/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("West neighbor type: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check the type of the current cell
def check_current_type(x_pos, y_pos):
    url = f'{base_url}/dpw/check-current-type/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("Current cell type: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check north neighbor's pheromone intensity
def check_north_pheromone(x_pos, y_pos):
    url = f'{base_url}/dpw/north-pheromone/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("North pheromone intensity: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check south neighbor's pheromone intensity
def check_south_pheromone(x_pos, y_pos):
    url = f'{base_url}/dpw/south-pheromone/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("South pheromone intensity: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check east neighbor's pheromone intensity
def check_east_pheromone(x_pos, y_pos):
    url = f'{base_url}/dpw/east-pheromone/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("East pheromone intensity: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check west neighbor's pheromone intensity
def check_west_pheromone(x_pos, y_pos):
    url = f'{base_url}/dpw/west-pheromone/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("West pheromone intensity: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check the pheromone intensity of the current cell
def check_current_pheromone(x_pos, y_pos):
    url = f'{base_url}/dpw/current-pheromone/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("Current pheromone intensity: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to check if the current pheromone has been visited
def check_if_visited(x_pos, y_pos):
    url = f'{base_url}/dpw/check-if-visited/{x_pos}/{y_pos}'
    response = requests.get(url)

    if response.status_code == 200:
        print("The current cell has been visited?: ", response.json()[0])
    else:
        print('Error:', response.status_code)
    return response.json()[0]

# Request to set the north neighbor's type
def set_north_neighbor(x_pos, y_pos, type):
    url = f'{base_url}/dpw/set-north-neighbor/{x_pos}/{y_pos}/{type}'
    response = requests.post(url)

    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Request to set the south neighbor's type
def set_south_neighbor(x_pos, y_pos, type):
    url = f'{base_url}/dpw/set-south-neighbor/{x_pos}/{y_pos}/{type}'
    response = requests.post(url)

    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Request to set the east neighbor's type
def set_east_neighbor(x_pos, y_pos, type):
    url = f'{base_url}/dpw/set-east-neighbor/{x_pos}/{y_pos}/{type}'
    response = requests.post(url)

    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Request to set the west neighbor's type
def set_west_neighbor(x_pos, y_pos, type):
    url = f'{base_url}/dpw/set-west-neighbor/{x_pos}/{y_pos}/{type}'
    response = requests.post(url)

    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

