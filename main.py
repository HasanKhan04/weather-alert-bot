import requests
from twilio.rest import Client


api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC5e4bace9eefaaa16e8e23b3b3f3eab5d"
auth_token = "c7f522d0d68d9ea1414cb9ac1d209c2c"
parameters = {
    "lat": 43.589046,
    "lon": -79.644119,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()
id_list = []

for i in range(0, 12):
    weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    id_list.append(int(weather_id))


def is_rain():
    for temp in id_list:
        if temp < 700:
            return True


if is_rain():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+15856326092',
        to='+14168389352'
    )
    new_message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+15856326092',
        to='+14166026965'
    )
    new_message2 = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+15856326092',
        to='+16476253852'
    )
    print(message.status)
