'''
import requests

# wildlife.py

import requests

def get_species_list():
    """
    Retrieves a list of species from a web service.
    
    Returns:
        list: A list of species dictionaries.
    """
    url = "https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle=-16.92,145.777,100000"
    response = requests.get(url)
    species_list = response.json()
    return species_list

# Debugging: Test the get_species_list() function
print(get_species_list())
'''


# wildlife.py
import requests

def get_species_list(coordinate, radius) -> list:
    """
    Retrieve a list of species in an area defined by a circle.
    
    Args:
        coordinate (tuple): Latitude and longitude coordinates as a tuple.
        radius (int): Radius of the search area in meters.
        
    Returns:
        list: A list of species dictionaries.
    """
    latitude, longitude = coordinate
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={latitude},{longitude},{radius}"
    print(url)
    response = requests.get(url)
    data = response.json()
    

    if "SpeciesSightingSummariesContainer" in data and "SpeciesSightingSummary" in data["SpeciesSightingSummariesContainer"]:
        species_list = [
            {
            "TaxonID": item.get("Species").get("TaxonID"),
            "AcceptedCommonName": item.get("Species").get("AcceptedCommonName"),
            "PestStatus": item.get("Species").get("PestStatus")
            }
            for item in data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
        ]
        return species_list
    else:
        return []

# Uncomment the following assert statements for testing
def test_get_species_list():
    # Test with a known location
    species_list = get_species_list((-16.92, 145.777), 100000)
    assert species_list is not None
    assert len(species_list) > 0
    print(species_list)

    # Test with an unknown location
    species_list = get_species_list((0, 0), 100000)
    assert species_list == []
    print(species_list)

 #test_get_species_list()


