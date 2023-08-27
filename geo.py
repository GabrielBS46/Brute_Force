from geopy.geocoders import Nominatim
import time
from pprint import pprint
import sys

app = Nominatim(user_agent="tutorial")

geo = sys.argv[1]

location = app.geocode(geo).raw

latitude = location["lat"]
longitude = location["lon"]
city = location["display_name"]

print(f"Segue coordenadas: {latitude},{longitude}")
print(city)

#print(location)
