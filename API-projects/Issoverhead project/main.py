import requests
from datetime import datetime
import smtplib

MY_LAT = 28.474388 # Your latitude
MY_LONG = 77.503990 # Your longitude

user = "YOUR MAIL ID"
password = "YOUR PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
if abs(iss_latitude-MY_LAT)<5 and abs(iss_longitude-MY_LONG)<5:
# and it is currently dark
    if time_now.hour > sunset or time_now.hour < sunrise:
# Then email me to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user,
                                to_addrs=user,
                                msg=f"Subject:Look up\n\nSee the ISS is above head")
# BONUS: run the code every 60 seconds.



