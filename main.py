#Task 1
#create menu

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
    print(f"{leftAlignment : <20}{rightAlignment : >30} ")

    # Option 2
    rightAlignment = "wildlife> exit"
    leftAlignment = "2. Exit the application "
    print(f"{leftAlignment : <20}{ rightAlignment : >27}")

    # Option 3
    leftAlignment = "3. Display animal species in a city"
    rightAlignment = "wildlife> species <city>"
    print(f"{leftAlignment : <20}{ rightAlignment : >27}")

    # Option 4
    leftAlignment = "4. Display animal sightings in a city "
    rightAlignment = "wildlife> sightings <city> <taxID> "









 















#Task 2
#function that: ...




'''
Task 2 User Input
Next, write a main() function that displays the help menu and then 
repeatedly prompts the user to input their command.
• The user should be prompted for a command with the 
following: “wildlife> ”
o If the user inputs help, the function should call 
display_menu() 
o If the user enters exit, then the system should exit.

'''
def main():
    display_menu()

    while True:
        userInput = input("Wildlife>").strip().lower() 
        print(f"The option that you have chosen is, {userInput}!")
        
        if userInput == "help" or userInput ==  "Display help":
            display_menu()
        elif userInput == "exit" or userInput == "Exit the application":
            print("Exit the Application")
            exit()
#Testing
#write display 2 options
# pass

if __name__ == "__main__":
    main()
















#Task 3
#function that:...


# TODO delete this function, since it has already been utilized before.
def display_menu():
    print("Menu:")
    print("1. Display animal species in a city")
    print("2. Other options...")

def searchSpecies(city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of species for any city
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(speciesList):
    print("Species found:")
    for species in speciesList:
        print(f"Common Name: {species['Species']['AcceptedCommonName']}, Pest Status: {species['Species']['PestStatus']}")

def main():
    display_menu()
    command = input("Enter command: ")

    if command.startswith("species"):
        # Extract the city from the command
        parts = command.split()
        if len(parts) > 1:
            city = parts[1]
            speciesList = searchSpecies(city)
            display_species(speciesList)
        else:
            print("Please provide a city after 'species'.")

if __name__ == "__main__":
    main()


#Task 4


def display_menu():
    print("Menu:")
    print("1. Display animal species in a city")
    print("2. Display animal sightings in a city")
    print("3. Other options...")

def searchSpecies(city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of species for any city
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil", "TaxonID": 1039}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous", "TaxonID": 1234}}
    ]

def searchSightings(taxonid, city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of sightings for any species and city
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_species(speciesList):
    print("Species found:")
    for species in speciesList:
        print(f"Common Name: {species['Species']['AcceptedCommonName']}, TaxonID: {species['Species']['TaxonID']}, Pest Status: {species['Species']['PestStatus']}")

def displaySightings(sightings):
    print("Sightings found:")
    for sighting in sightings:
        print(f"Start Date: {sighting['properties']['StartDate']}, Locality: {sighting['properties']['LocalityDetails']}")

def main():
    display_menu()
    command = input("Enter command: ")

    if command.startswith("species"):
        # Extract the city from the command
        parts = command.split()
        if len(parts) > 1:
            city = parts[1]
            speciesList = searchSpecies(city)
            display_species(speciesList)
        else:
            print("Please provide a city after 'species'.")
    elif command.startswith("sightings"):
        # Extract species and city from the command
        parts = command.split()
        if len(parts) > 2:
            species, city = parts[1], parts[2]
            sightings = searchSightings(species, city)
            displaySightings(sightings)
        else:
            print("Please provide both species and city after 'sightings'.")

if __name__ == "__main__":
    main()





























#Task 4
#function that:...
