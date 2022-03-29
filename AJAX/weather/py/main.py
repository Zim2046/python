import requests
from pprint import pprint

key = '755e9a004354c21722013d90cd4aca31'
lat = '32.78240'
lon = '117.11293'


def get_weather_data():
    res = requests.get(endpoint)
    return res.json()
    
