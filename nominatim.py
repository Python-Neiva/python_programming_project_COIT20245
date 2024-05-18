import requests

def gps_coordinate(city) -> dict:
    """
    Retrieves the GPS coordinates (latitude and longitude) of a given city using the Nominatim API.

    Parameters:
    city (str): The name of the city for which to retrieve the GPS coordinates.

    Returns:
    dict: A dictionary containing the latitude and longitude of the city. If the city is not found or an error occurs,
          default coordinates for Brisbane (-27.4689682, 153.0234991) are returned.
    """
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
    print(coord)
    assert coord == {"latitude": -27.4689682, "longitude": 153.0234991}
    print("GPS coordinate function works correctly.")

    # Testing with other cities
    coord = gps_coordinate("Sydney")
    print(coord)
    assert coord == {"latitude": -33.8698439, "longitude": 151.2082848}
    print("GPS coordinate function works correctly for Sydney.")

    coord = gps_coordinate("Melbourne")
    print(coord)
    assert coord == {"latitude": -37.8142454, "longitude": 144.9631732}
    print("GPS coordinate function works correctly for Melbourne.")

    coord = gps_coordinate("Perth")
    print(coord)
    assert coord == {"latitude": -31.9558933, "longitude": 115.8605855}
    print("GPS coordinate function works correctly for Perth.")
