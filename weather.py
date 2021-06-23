import requests
import os
import sys
from datetime import datetime

api_key = 'addcc2af5b525039110a35826f4d328d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} °„C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


data={'city':location,
      'date & time':date_time,
      'temp(°„C)':temp_city,
      'weather desc':weather_desc,
      'humidity':hmdt,
      'wind(kmph)':wind_spd}

#Data saving to a file
file = open("Data.txt", "a")
str_data= repr(data)
file.write("Data = " + str_data + "\n")
file.close()

#Search history
x=input("\nDo you want to see all the search history(Y/N): ")
if x=='y' or x=='Y':
  with open("Data.txt","r") as fp:
    print(fp.read())
  z=input("Do you want to delete all search history(Y/N): ")
  if z=='y' or z=='Y':
    f = open("Data.txt","w")
    f.truncate()
    f.close()
    print('Search history successfuly cleard')
  else:
    sys.exit("Successful termination")   
else:
  sys.exit("Successful termination")
