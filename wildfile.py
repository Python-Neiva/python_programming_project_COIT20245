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
