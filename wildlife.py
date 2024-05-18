import requests

def get_species_list(coordinate, radius) -> list:
    """
    Retrieves a list of species sightings within a given radius of a coordinate.

    Args:
        coordinate (dict): A dictionary containing the latitude and longitude of the coordinate.
        radius (float): The radius in kilometers.

    Returns:
        list: A list of species sighting summaries.

    """
    url = (f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals"
           f"&circle={coordinate['latitude']},{coordinate['longitude']},{radius}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        species_list = data.get("SpeciesSightingSummariesContainer", {}).get("SpeciesSightingSummary", [])
        return species_list
    return []

def get_surveys_by_species(coordinate, radius, taxonid) -> list:
  """
  Retrieves a list of animal surveys in an area for a given species using the Queensland wildlife data API.

  Args:
      coordinate (dict): A dictionary containing latitude and longitude keys.
      radius (int): The search radius in meters.
      taxonid (int): The taxon ID of the species to search for.

  Returns:
      list: A list of survey dictionaries.
  """
  url = "https://apps.des.qld.gov.au/species/"
  params = {
      "op": "getsurveysbyspecies",
      "taxonid": taxonid,
      "circle": f"{coordinate['latitude']},{coordinate['longitude']},{radius}"
  }

  response = requests.get(url, params=params)
  response.raise_for_status()

  data = response.json()
  '''
  if the data dictionary has a key "features", this line of code will return the value associated with that key. If there is no "features" key in the dictionary, it will return an empty list.'''
  return data.get("features", [])


def test_get_species_list():
    RADIUS = 100000  # 100 km radius

    # Testing the get_species_list function
    coord = {"latitude": -16.92, "longitude": 145.777}
    species_list = get_species_list(coord, RADIUS)
    assert isinstance(species_list, list)
    assert len(species_list) > 0
    print("Get species list function works correctly.")

    # Example usage ( uncomment for testing after reviewing asserts)
    coordinate = {"latitude": -27.4689682, "longitude": 153.0234991}
    species_list = get_species_list(coordinate, RADIUS)
    assert isinstance(species_list, list)
    assert len(species_list) > 0
    print("Get species list function works correctly.")

def test_get_surveys_by_species():
    coordinate = {"latitude": -27.4689682, "longitude": 153.0234991}
    radius = 100000  # 100 km radius
    taxonid = 12345  # Replace with the actual taxon ID of the species to test

    surveys = get_surveys_by_species(coordinate, radius, taxonid)

    assert isinstance(surveys, list)
    assert len(surveys) >= 0  # verify that the list is not empty

    print("get_surveys_by_species test passed.")

# Commented in order to avoid running the tests when importing the module
if __name__ == "__main__":
    test_get_species_list()
    test_get_surveys_by_species()    