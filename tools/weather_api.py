from agents import function_tool
from dotenv import load_dotenv,find_dotenv
import requests
import os
load_dotenv(find_dotenv(),override=True)

api_key = os.getenv("WEATHER_API_KEY")


base_url = "http://api.weatherapi.com/v1/current"

get_api = requests.get(f"{base_url}.json?key={api_key}&q=Karachi") # this is not working so instead of this we use longitude and latitude for fething weather updates
 

@function_tool
def get_weather(city:str):
    """get the current weather update"""
    print("Weather tool is called...")
    if city.lower().strip() == "karachi":
        get_api = requests.get(f"{base_url}.json?key={api_key}&q=24.8607,67.0011")
        responce = get_api.json()
        return responce["current"]
    
    elif city.lower().strip() == "islamabad":
        get_api = requests.get(f"{base_url}.json?key={api_key}&q=33.6844,73.0479")
        responce = get_api.json()
        return responce["current"]

    elif city.lower().strip() == "lahore":
        get_api = requests.get(f"{base_url}.json?key={api_key}&q=31.5497,74.3436")
        responce = get_api.json()
        return responce["current"]
    else:
        return f" weather update dont found"
    
