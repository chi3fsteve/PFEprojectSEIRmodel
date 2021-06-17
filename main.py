import pandas as pd

df = pd.read_csv('geolocations.csv')

dictionary = df.to_dict()
dictionary.pop('Unnamed: 0')

addresses = df.Address.to_list()
latitude = df.latitude.to_list()
longitude = df.longitude.to_list()
print(longitude)