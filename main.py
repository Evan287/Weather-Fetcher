import requests

API_KEY = "75b32f8731760ad37a7d41c006c54256"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" # f string allows directly embedding variable and expressions inside of a string
#HTTP requests
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather: ", weather)
    print("Temperature: ", temperature, "celcius")
else: 
    print("An error has occured.")
