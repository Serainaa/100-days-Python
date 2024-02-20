import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = 39.387387
MY_LNG = 22.940689
MY_EMAIL = "seraina7@yahoo.gr"
PASSWORD = ""

# Parameters for API requests
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

# Function to check if the ISS is near the current location
def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

# Function to check if it's currently night time
def is_night():
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(':')[0])
    today = int(datetime.now().hour)

    if today >= sunset or today <= sunrise:
        return True

# Continuously check if conditions are met to send an email
while True:
    time.sleep(60)  # Check every minute
    
    if is_near() and is_night():
        # If the ISS is near and it's night, send an email notification
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Look up!\n\nThe ISS is above you in the sky")
