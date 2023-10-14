from io import BytesIO
import requests
from PIL import Image

img = ''


def API(m):
    global img
    s = 'Санкт-Петербург,'
    toponym_to_find = s + m
    print(toponym_to_find)

    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "5e3d492d-da55-4b30-b588-561714e7d959",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    toponym_coodrinates = toponym["Point"]["pos"]

    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    delta = "0.005"

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude, 'flag~28.969573,41.04311'])
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    img = Image.open(BytesIO(response.content))
