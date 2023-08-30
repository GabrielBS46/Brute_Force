import ipinfo
import sys
from geopy.geocoders import Nominatim
from pprint import pprint
from  socket import gethostbyname

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Localizacao IP")
print(ascii_banner)

# Colocar Endereço na linha de comando
try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None
# Token do ipinfo.io
access_token = 'e7021c81aa341c'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails(gethostbyname(ip_address))

# Conversão dos valores em strings
for key, value in details.all.items():
#    print(f"{key}: {value}")
    if (key == 'ip'):
        print("Endereço IP",value)
    if (key == 'loc'):
        geo = value

### Geo Location IP - Usando coordenadas
app = Nominatim(user_agent="tutorial")

location = app.geocode(geo).raw

latitude = location["lat"]
longitude = location["lon"]
city = location["display_name"]

print(f"Segue coordenadas: {latitude},{longitude}")
print(city)
