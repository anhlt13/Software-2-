import requests
import json

from sympy.physics.units import temperature

user = input(f"Enter a municipality: ")
api_key = "90ca21f1ca4fe12d7f78219302f32b4c"


try:
    request_city = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user}&limit=5&appid={api_key}")

    if request_city.status_code == 200:
        response_city = request_city.json()
        for city in response_city:
            latitude =city["lat"]
            longitude =city["lon"]
        try:
            request_weather_data = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid=90ca21f1ca4fe12d7f78219302f32b4c"
            response_weather_data = requests.get(request_weather_data)
            if response_weather_data.status_code == 200:
                respond_weather = response_weather_data.json()
                weather_data = respond_weather["current"]["weather"][0]
                description = weather_data["description"]
                temperature = int(respond_weather["current"]["temp"])
                print(f"Current weather is: {description}")
                print(f"Current temperature is: {temperature-273.15:.2f} Celsius degree")
        except requests.exceptions.RequestException as error:
            print(f"Error", error)
except requests.exceptions.RequestException as error:
    print(f"Request could not be completed")

