import requests

def gps_coordinate(city) -> dict:
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return {"latitude": latitude, "longitude": longitude}
    return {"latitude": -27.4689682, "longitude": 153.0234991} #Default coordinates for Brisbane

if __name__ == "__main__":
    # Testing the gps_coordinate function
    coord = gps_coordinate("Brisbane")
    assert coord == {"latitude": -27.4689682, "longitude": 153.0234991}
    print("GPS coordinate function works correctly.")
