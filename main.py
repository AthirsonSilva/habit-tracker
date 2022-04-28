import requests
from datetime import datetime

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'athirson'
TOKEN = 'pixela-token'
GRAPH_ID = 'my1graph'

params = {
    'token': USERNAME,
    'username': TOKEN,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


def send_info():
    response = requests.post(url=PIXELA_ENDPOINT, json=params)
    print(response.text)


graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'kuro'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

today_date = datetime.now()
today = today_date.strftime('%Y%m%d')
pixel_data = {
    'date': today,
    'quantity': '1',
}

pixel_data_updated = {
    'quantity': '1'
}

pixel_creation = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_update = f'{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime("%Y%m%d")}'


def create_graph():
    response = requests.post(
        url=graph_endpoint, json=graph_config, headers=headers)
    print(response)


def create_pixel():
    response = requests.post(
        url=pixel_creation, json=pixel_data, headers=headers)
    print(response.text)


def update_pixel():
    response = requests.put(
        url=pixel_update, json=pixel_data_updated, headers=headers)
    print(response.text)


update_pixel()
