import requests
from client.config import Config

base_url = Config.BASE_URL

def initiate_territory(territory_file_path):
    url = f'{base_url}/territory/initiate?territory_file_path={territory_file_path}'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

def delete_territory():
    url = f'{base_url}/territory/remove'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

def reset_territory():
    url = f'{base_url}/territory/reset'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Error:', response.status_code)
    return response.text

def check_exploration():
    url = f'{base_url}/territory/check-exploration'
    response = requests.get(url)
    if response.text == "True":
        print("There are missing cells to explore!")
        return True
    else:
        print("All cells in the territory have been explored!")
        return False
