"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
jsondata = response.json()
print(type(jsondata))
#print(jsondata)
print("langitude =",jsondata['coord']['lon'])
print("latitude =",jsondata['coord']['lat'])
print("weather condition =",jsondata['weather'])
print("Wind Speed-",jsondata['wind'])
print("Sunset-",jsondata['sys']['sunset'])
print("Sunrise-",jsondata['sys']['sunrise'])
print("Setuptiming-",jsondata['timezone'])


