import requests
from client.config import Config

'''This file contains all the client requests that can be made to create, reset and delete the territory in the DB'''

base_url = Config.BASE_URL

# Requests to create all the nodes and the relations between them in the DB
def initiate_territory(territory_file_path):
    url = f'{base_url}/territory/initiate?territory_file_path={territory_file_path}'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Requests to delete all nodes and relations in the DB
def delete_territory():
    url = f'{base_url}/territory/remove'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Requests to reset the territory in the DB
def reset_territory():
    url = f'{base_url}/territory/reset'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

# Requests to check if there are cells that haven't been visited
def check_exploration():
    url = f'{base_url}/territory/check-exploration'
    response = requests.get(url)
    if response.text == "True":
        print("There are missing cells to explore!")
        return True
    else:
        print("All cells in the territory have been explored!")
        return False
