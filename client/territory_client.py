import requests
from config import Config

base_url = Config.BASE_URL

def initiate_territory():
    url = f'{base_url}/territory/initiate'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.json())
        status = "Territory successfully created!"
    else:
        print('Error:', response.status_code)
        status = "An error occur while loading the file."
    return status

def delete_territory():
    url = f'{base_url}/territory/remove'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.json())
        status = "Territory successfully deleted!"
    else:
        print('Error:', response.status_code)
        status = "An error occur while deleting the territory."
    return status

def reset_territory():
    url = f'{base_url}/territory/reset'
    response = requests.post(url)
    if response.status_code == 200:
        print(response.json())
        status = "Territory successfully reset!"
    else:
        print('Error:', response.status_code)
        status = "An error occur while resetting the file."
    return status

reset_territory()
