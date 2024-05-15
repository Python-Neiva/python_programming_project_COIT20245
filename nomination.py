import requests
import json

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()
    
    if data:
        # Extract the latitude and longitude from the first result
        latitude = float(data[0]['lat'])
        longitude = float(data[0]['lon'])
        return {"latitude": latitude, "longitude": longitude}
    else:
        return None
print(gps_coordinate("Cairns"))