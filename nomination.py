import requests
import json

def gps_coordinate(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()
    
    if data:
        # Extract the latitude and longitude from the first result
        result = data[0]
        latitude = float(result['lat'])
        longitude = float(result['lon'])
        return {"latitude": latitude, "longitude": longitude}
    else:
        return None #special data type that indicates that thre is none data.

def test_gps_coordinate():
    # Test with a known city
    coordinates = gps_coordinate("Cairns")
    assert coordinates == {"latitude": -16.9206657, "longitude": 145.7721854}
    
    # Test with an unknown city
    coordinates = gps_coordinate("Unknown City")
    assert coordinates == None
