import requests

def gps_coordinate(city: str) -> dict:
    """
    Retrieves the GPS coordinates (latitude and longitude) of a given city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: A dictionary containing the latitude and longitude of the city.
              The dictionary has the following structure:
              {
                  "latitude": <float>,
                  "longitude": <float>
              }

              If the city is not found or there is no data available, None is returned.
    """
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()
    
    if data:
        # Extract the latitude and longitude from the first result and convert data type into float
        result = data[0]
        latitude = float(result['lat'])
        longitude = float(result['lon'])
        return {"latitude": latitude, "longitude": longitude}  # Return the dictionary with the latitude and longitude
    else:
        return {}  # Return a empty dictionary.

def test_gps_coordinate():
    # Test with a known city
    coordinates = gps_coordinate("Cairns")
    assert coordinates == {"latitude": -16.9206657, "longitude": 145.7721854}
    
    # Test with an unknown city
    coordinates = gps_coordinate("Unknown City")
    print(coordinates)
    assert coordinates == {}

#test_gps_coordinate()
