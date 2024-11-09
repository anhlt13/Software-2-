import requests
import json


request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        joke_text = response.json()
        print(joke_text["value"])
except requests.exceptions.RequestException as e:
        print("Request could not be completed.")


