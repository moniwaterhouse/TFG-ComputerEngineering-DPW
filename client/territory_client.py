import requests
from config import Config

base_url = Config.BASE_URL

def initiate_territory():
    url = f'{base_url}/territory/initiate'
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
