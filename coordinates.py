from geopy.geocoders import GoogleV3
import pandas as pd
import json

geolocator = GoogleV3(api_key="Your API key")


with open('ulice.txt', encoding='utf-8') as f:
    lines = f.readline()
content = lines.split('ul.')
content.pop(0)
content = [i.lstrip() for i in content]

print(content)
addresses = []
latitude = []
longitude = []

for i in content:
    location = geolocator.geocode(i, timeout=10)
    if location is not None and location.address[:len(i)-7] == i[:len(i)-7]:
        addresses.append(location.address)
        latitude.append(str(location.latitude))
        longitude.append(str(location.longitude))
    else:
        continue

dictionary = {'Address': addresses, 'latitude': latitude, 'longitude': longitude}

df = pd.DataFrame(dictionary)
df.to_csv('geolocations.csv')