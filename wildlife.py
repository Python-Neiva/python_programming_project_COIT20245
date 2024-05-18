import requests

def get_species_list(coordinate, radius):
    url = (f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals"
           f"&circle={coordinate['latitude']},{coordinate['longitude']},{radius}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        species_list = data.get("SpeciesSightingSummariesContainer", {}).get("SpeciesSightingSummary", [])
        return species_list
    return []

if __name__ == "__main__":
    # Testing the get_species_list function
    coord = {"latitude": -16.92, "longitude": 145.777}
    species_list = get_species_list(coord, 100000)
    assert isinstance(species_list, list)
    print("Get species list function works correctly.")

def get_surveys_by_species(coordinate, radius, taxonid):
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

# Example usage ( #TODO uncomment for testing after implementing asserts)
# coordinate = {"latitude": -27.4689682, "longitude": 153.0234991}
# species_list = get_species_list(coordinate, RADIUS)
# print(species_list)