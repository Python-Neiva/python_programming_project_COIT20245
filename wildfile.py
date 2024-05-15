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

def get_species_list(coordinate, radius):
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
    response = requests.get(url)
    data = response.json()
    
    if "SpeciesSightingSummariesContainer" in data:
        species_list = data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
        return species_list
    else:
        return None

# Uncomment the following assert statements for testing
# assert get_species_list((-16.92, 145.777), 100000) is not None
# assert len(get_species_list((-16.92, 145.777), 100000)) > 0
