
import requests
from twilio.rest import Client
MY_LAT=36.778259
MY_LONG=-119.417931
TWILIO_ACCOUNT_SID="734582734950374295"
TWILIO_AUTH_TOKEN="74235473029734547358"




account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN


params={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":"5432978347958347895",
    "exclude":"current,minutely,daily"

}
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=params)
response.raise_for_status()
data=response.json()

weather=[]
count=0
for i in range(0,12):
    weather.append(data["hourly"][4]["weather"][0]["id"])
    if data["hourly"][i]["weather"][0]["id"]<800:
        count+=1

if count>0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+13432075967',
        to='+14327549832'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not raining!",
        from_='+134320759',
        to='+14327549832'
    )






