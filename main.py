import sys


RADIUS = 100000  # 100 km radius

def display_menu():
    """
    This function displays a menu with numbered options.

    """
    print("Help")
    print("====")
    print("The following commands are recognized:")

    # Option 1
    rightAlignment = "wildlife> help"
    leftAlignment = "1. Display help"
    print(f"{leftAlignment : <35}{rightAlignment : >55} ")

    # Option 2
    rightAlignment = "wildlife> exit"
    leftAlignment = "2. Exit the application "
    print(f"{leftAlignment : <35}{ rightAlignment : >55}")

    # Option 3
    leftAlignment = "3. Display animal species in a city"
    rightAlignment = "wildlife> species <city>"
    print(f"{leftAlignment : <35}{ rightAlignment : >55}")

    # Option 4
    leftAlignment = "4. Display animal sightings in a city"
    rightAlignment = "wildlife> sightings <city> <tax ID>"
    print(f"{leftAlignment : <35}{ rightAlignment : >55}")

    # Option 5
    leftAlignment = "5. Display venonmous species wildlife"
    rightAlignment = "wildlife> species <city> venomous"
    print(f"{leftAlignment : <35}{ rightAlignment : >55}")

    
def main():
    """
    Main function that runs the wildlife application.
    """
    display_menu()
    while True:
        command = input("wildlife> ").strip().lower().split()
        INVALID_COMMAND_MSG = "Invalid command. Please try again."

        if len(command) == 0:
            print(INVALID_COMMAND_MSG)
            continue
        if command[0] == "help":
            display_menu()
        elif command[0] == "exit":
            sys.exit()
        elif command[0] == "species":
            if len(command) == 2:
                city = command[1]
                species_list = search_species(city)
                display_species(species_list)
            elif len(command) == 3 and command[2] == "venomous":
                city = command[1]
                species_list = search_species(city)
                # uncomment to run the function that asserts the function filter_venomous
                # test_filter_venomous()
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                print(INVALID_COMMAND_MSG)
        elif command[0] == "sightings":
            if len(command) == 3:
                city = command[1]
                taxon_id = command[2]
                sightings = search_sightings(taxon_id, city)
                display_sightings(sightings)
            else:
                print(INVALID_COMMAND_MSG)
        else:
            print(INVALID_COMMAND_MSG)

import wildlife
import nominatim

def search_species(city):
    #test function for test_gps, which is used in thi function, uncomment to run the test
    # test_gps()
    coordinate = gps(city)
    species_list = wildlife.get_species_list(coordinate, RADIUS)

    return species_list

def display_species(species_list):
    for species in species_list:
        common_name = species["Species"]["AcceptedCommonName"]
        pest_status = species["Species"]["PestStatus"]
        print(f"Species: {common_name}, Pest Status: {pest_status}")


def display_sightings(sightings):
    # Sort sightings by date first
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        date = sighting["properties"]["StartDate"]
        location = sighting["properties"]["LocalityDetails"]
        print(f"Sighting Date: {date}, Location: {location}")

def filter_venomous(species_list):
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

# Assert function for filter_venomous
def test_filter_venomous():
    species_list = [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
        {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}},
        {"Species": {"AcceptedCommonName": "lizard", "PestStatus": "Nil"}},
    ]
    venomous_species = filter_venomous(species_list)
    assert len(venomous_species) == 2
    assert venomous_species[0]["Species"]["AcceptedCommonName"] == "snake"
    assert venomous_species[1]["Species"]["AcceptedCommonName"] == "spider"
    print("Filter venomous species test passed.")


def gps(city) -> dict:
    # Default coordinates for Brisbane (for testing purposes)
    # return { "latitude": -27.4689682, "longitude": 153.0234991 }
    return nominatim.gps_coordinate(city)

def test_gps():
    result = gps("Brisbane")
    assert result == {"latitude": -27.4689682, "longitude": 153.0234991}
    print("GPS test passed.")

# Functions for Task 9 - Retrieving sightings

def search_sightings(taxonid, city) -> list:
    """

    Retrieves a list of animal sightings in a city for a given species (optional).

    Args:
        taxonid (int): The taxon ID of the species to search for (optional).
        city (str): The name of the city.

    Returns:
        list: A list of sighting dictionaries.
    """

    # Default sightings data for testing purposes
    # return [{"properties":{"StartDate":"1999-11-15","LocalityDetails":"Tinaroo"}}]

    if not city:
        print("Error: Please specify a city for searching sightings.")
        return []

    coordinate = nominatim.gps_coordinate(city)

    surveys = wildlife.get_surveys_by_species(coordinate, RADIUS, taxonid)
    '''This line of code is creating a new list that contains only the surveys where the "SiteCode" is "INCIDENTAL". by using a list comprehension'''
    filtered_surveys = [survey for survey in surveys if survey["properties"]["SiteCode"] == "INCIDENTAL"]
    return filtered_surveys

#task 10 - earliest sighting
def sort_by_date(sightings):
    """
    Sorts a list of sightings by their start dates in ascending order.

    Args:
        sightings (list): A list of sighting dictionaries.

    Returns:
        list: A new list of sightings sorted by earliest start date first.
    """
    # Implementing insertion sort algorithm
    for i in range(1, len(sightings)):
        # This is the element we want to position in its correct place
        key = sightings[i]

        # Initialize the variable that will be used to find the correct position of the element referenced by `key` sometimes called `key_item` in this algorithm
        j = i - 1

        # Move elements of `sightings[0..i-1]`, that are greater than `key`, to one position ahead of their current position
        while j >= 0 and sightings[j]["properties"].get("StartDate", "") > key["properties"].get("StartDate", ""):
            # Move the element to the right
            sightings[j + 1] = sightings[j]
            j -= 1
        
        # Insert the element in its correct position, which is `j + 1`, because we decremented `j` in the last step.
        sightings[j + 1] = key
    return sightings


if __name__ == "__main__":
    main()
