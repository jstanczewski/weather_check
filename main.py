import urllib.request
import json
from decouple import config
from datetime import datetime

api_endpoint = 'http://api.openweathermap.org/data/2.5/weather'
while True:
    city = input('Type the name of the city for which You want to know the weather. Type \'no\' if You want to quit the app. ')
    apikey = config('API_KEY')
    units = 'metric'
    url = api_endpoint + '?q=' + city + '&appid=' + apikey + '&units=' + units
    url = url.replace(' ', '%20')

    with open('cities_names_list.txt') as f:
        cities_names = f.read()

    if city.lower() == 'no':
        break
    elif f"{', ' + city.lower() + ', '}" in cities_names:

        response = urllib.request.urlopen(url)
        parse_response = json.loads(response.read())

        temperature = parse_response['main']['temp']
        weather_desc = parse_response['weather'][0]['description']
        time = datetime.utcfromtimestamp(int(parse_response['dt'])).strftime('%H:%M:%S %d.%m.%Y')
        sunrise_hour = datetime.utcfromtimestamp(int(parse_response['sys']['sunrise'])).strftime('%H:%M')
        sunrise_day_en = datetime.utcfromtimestamp(int(parse_response['sys']['sunrise'])).strftime('%B %d')
        sunset_hour = datetime.utcfromtimestamp(int(parse_response['sys']['sunset'])).strftime('%H:%M')
        sunset_day_en = datetime.utcfromtimestamp(int(parse_response['sys']['sunset'])).strftime('%B %d')

        print(f'Weather data for the city of {city.capitalize()}:')
        print(f'Temperature (Celsius) - {temperature}')
        print(f'Weather description - {weather_desc}')
        print(f'Time of the reading (UTC) - {time}')
        print(f'On {sunrise_day_en} The Sun rises at: {sunrise_hour} (UTC)')
        print(f'On {sunset_day_en} The Sun sets at: {sunset_hour} (UTC)')

    else:
        print(f'Sorry, there is no city called {city} in our database.')

    print('\n')
