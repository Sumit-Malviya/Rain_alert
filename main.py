import requests

api_key = "69f04e4613056b159c2761a9d9e664d2"

parameters = {

    "lat": 30.723856,
    "lon": 79.274367,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather_slice = data["hourly"][0:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring your Umbrella")




