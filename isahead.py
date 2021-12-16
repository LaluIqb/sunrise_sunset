import requests, smtplib, time
from datetime import datetime

MY_LAT, MY_LONG = -7.408320, 112.673561


def iss_in_sight(current_lat, current_long):
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if abs(current_lat - iss_latitude) <= 0 and abs(current_long - iss_longitude) <= 0:
        return True
    else:
        return False


def is_night():
    parameter = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameter)
    response.raise_for_status()

    data = response.json()
    sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_hour = int(data['results']['sunset'].split('T')[1].split(':')[0])

    now_hour = datetime.now().hour

    if sunset_hour <= now_hour <= sunrise_hour:
        return True


while True:
    if iss_in_sight(MY_LAT, MY_LONG) and is_night():

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user='_@gmail.com', password='_')
            connection.sendmail(
                from_addr='_@gmail.com',
                to_addrs='_@yahoo.com',
                msg='Subject:Look!\n\nLook up the ISS is above you in the sky.')

    time.sleep(60)
