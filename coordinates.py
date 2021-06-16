from geopy.geocoders import GoogleV3

geolocator = GoogleV3(api_key="AIzaSyBotFlB3ie26_5GLUtjr0BVfs7fixVWZZA")


with open('ulice.txt', encoding='utf-8') as f:
    lines = f.readline()
content = lines.split('ul.')
content.pop(0)
content = [i.lstrip() for i in content]

print(content)


location = geolocator.geocode(content[2], timeout=10)
print(location.latitude, location.longitude, location.address)