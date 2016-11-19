# coding: utf-8

import urllib3
from urllib import parse
import pyowm	#Open Weather Map (here OWP)	! REQUIERE PIP INSTALLATION !


#Free API vars
USER_NUMBER = "12345678"
USER_KEY = "usb42qe7g2n8r"

#OWP vars
API_OWM = "API KEY HERE !"	#https://home.openweathermap.org for api key
city = "Paris,FR"	#Most beautifull city in the world ^^

#======================================
#	   Configuring SMS sending
#======================================

http = urllib3.PoolManager()

#======================================
#	  Catch weather of your city
#======================================

owm = pyowm.OWM(API_OWM)
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = round(w.get_temperature('celsius')["temp"],1)

if -10.0 >= temperature:
	msg = "Ho ! It's very, very cold today ! {temp} only ! Good luck ^^".format(temp = str(temperature) + " °C ")

elif -10.0 < temperature <= 0.0:
	msg = "It's cold today, {temp} only, don't catch cold !".format(temp = str(temperature) + " °C ")

elif 0.0 < temperature <=10.0:
	msg = "Brouh ! It's not hot today, {temp} only. See you soon !".format(temp = str(temperature) + " °C")

elif 10.0 < temperature <=20.0:
	msg = "It's a beautiful day ahead ! {temp}, have a good day !".format(temp = str(temperature) + " °C")

elif 20.0 < temperature <=30.0:
	msg = "Waw ! So hot, enjoy ! {temp}. (And remember, drink water !).".format(temp = str(temperature) + " °C")

elif 30.0 < temperature <=40.0:
	msg = "My silicon circuits are melting under this {temp}, I will go to sleep in the fridge. Have a good day !".format(temp = str(temperature) + " °C")

else:
	msg = "The temperature is currently {temp}. Have a good day !".format(temp = str(temperature) + " °C")

msg = parse.quote(msg)
url = "https://smsapi.free-mobile.fr/sendmsg?user={user}&pass={passw}&msg={msg}".format(user = USER_NUMBER, passw = USER_KEY, msg = msg)
r = http.request('POST', url)

if int(r.status) == 200:
	print("Operation succes.")
else:
	print("Error: " + str(r.status))