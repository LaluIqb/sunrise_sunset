import requests
from datetime import datetime

MY_LAT, MY_LONG = -7.408320, 112.673561

parameter = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameter)
response.raise_for_status()

data = response.json()
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise_hour, sunset_hour)

now = datetime.now().hour
print(now)
