import os
from dotenv import load_dotenv
import requests

def main():

    load_dotenv()

    user_res = input("What city's weather would you like to look at?")
    
    weather_key = os.getenv("WEATHER_API_KEY")

    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_res}&appid={weather_key}&units=metric"

    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            raise Exception(f" Could not connect to API, {response.status_code}")

        result = response.json()

        print(f"City: {result['name']}")
        print(f"Temperature: {result['main']['temp']}°C")
        print(f"Weather: {result['weather'][0]['description']}")

    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    main()