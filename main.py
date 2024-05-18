import sys


RADIUS = 100000  # 100 km radius

def display_menu():
    print("Help")
    print("====")
    print("The following commands are recognised.")
    print("Display help wildlife> help")
    print("Exit the application wildlife> exit")
    print("Display animal species in a city wildlife> species <City>")
    print("Display animal sightings in a city wildlife> sightings <City> <TaxonID>")
    print("Display venomous species wildlife> species <City> venomous")

def main():
    display_menu()
    while True:
        command = input("wildlife> ").strip().split()
        if len(command) == 0:
            print("Invalid command. Please try again.")
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
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                print("Invalid command. Please try again.")
        elif command[0] == "sightings":
            if len(command) == 3:
                city = command[1]
                taxon_id = command[2]
                sightings = search_sightings(taxon_id, city)
                display_sightings(sightings)
            else:
                print("Invalid command. Please try again.")
        else:
            print("Invalid command. Please try again.")
from wildlife import get_species_list
from nominatim import gps_coordinate

def search_species(city):
    coordinate = gps(city)
    species_list = get_species_list(coordinate, RADIUS)
    return species_list

def display_species(species_list):
    for species in species_list:
        common_name = species["Species"].get("AcceptedCommonName", "Unknown")
        pest_status = species["Species"].get("PestStatus", "Unknown")
        print(f"Species: {common_name}, Pest Status: {pest_status}")

def search_sightings(taxon_id, city):
    # Stub function
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]
def display_sightings(sightings):
    for sighting in sightings:
        date = sighting["properties"].get("StartDate", "Unknown Date")
        location = sighting["properties"].get("LocalityDetails", "Unknown Location")
        print(f"Sighting Date: {date}, Location: {location}")

def filter_venomous(species_list):
    return [species for species in species_list if species["Species"].get("PestStatus") == "Venomous"]

def gps(city):
    return gps_coordinate(city)

if __name__ == "__main__":
    main()
