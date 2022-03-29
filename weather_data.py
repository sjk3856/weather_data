import requests
import os
from datetime import datetime

user_api = '#enter your api key'
location = input('Enter the city name: ')

#http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
complete_api_link = 'http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+user_api

#GET 방식으로 요청함
api_link = requests.get(complete_api_link)
#RESPONSE받음
api_data = api_link.json()

if api_data['cod'] =='404':
    print("Invalid City: {}, Please check your City name.".format(location))

else:
    #섭씨온도 = 절대온도 - 273도
    temp_city = ((api_data['main']['temp']) - 273.15)
    #[0]은 weather 리스트의 첫번째 요소로 접근했다는 의미
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("==============================================================")
    print("Weather Stats for - {} || {}".format(location.upper(),date_time))
    print("==============================================================")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc: ",weather_desc)
    print("Current Humidity: ",hmdt, '%')
    print("Current wind speed: ", wind_spd, 'kmph')

    #유튜브 강의 = https://youtu.be/w-V1pMrGAjc