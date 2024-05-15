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
    print(f"{leftAlignment : <20}{ rightAlignment : >27}")









 





























#Task 3
#function that:...

def search_species(city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of species for any city
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(speciesList):
    print("Species found:")
    for species in speciesList:
        acceptedName = species['Species']['AcceptedCommonName']
        pestStatus = species['Species']['PestStatus']
        print(f"Common Name: {acceptedName}, Pest Status: {pestStatus}")





#Task 4

def search_species(city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of species for any city
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil", "TaxonID": 1039}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous", "TaxonID": 1234}}
    ]

def search_sightings(taxonid, city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of sightings for any species and city
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_species(speciesList):
    print("Species found:")
    for species in speciesList:
        acceptedName = species['Species']['AcceptedCommonName']
        taxonID = species['Species']['TaxonID']
        pestStatus = species['Species']['PestStatus']

        print(f"Common Name: {acceptedName}, TaxonID: {taxonID}, Pest Status: {pestStatus}")

def display_sightings(sightings):
    print("Sightings found:")
    for sighting in sightings:
        startDate = sighting['properties']['StartDate']
        LocalityDetails = sighting['properties']['LocalityDetails']
        print(f"Start Date: {startDate}, Locality: {LocalityDetails}")
        ## TODO make text more descriptive, like: whipsnake was sighted at Tinaroo, Cairns in 2013



#Task 5

















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

        if userInput == "exit" or userInput == "Exit the application":
            print("Exit the Application")

        if userInput.startswith("species"):
        # Get the city from the command
            city = userInput.split()[1]
            speciesList = search_species(city)
            display_species(speciesList)

        if userInput.startswith("sightings"):
            # Extract species and city from the command
            speciesAndCity = userInput.split()
            # Validate that the user input includes city and sightings
            if len(speciesAndCity) > 2:
                species, city = speciesAndCity[1], speciesAndCity[2]
                sightings = search_sightings(species, city)
                display_sightings(sightings)
            else:
                print("Please provide both species and city after 'sightings'.")

        '''
        If none of the above options work,
        the selected option is taken as an error,
        and the menu with the options is displayed again.'''
        
        print("Please, select one of the given options")
        display_menu()
        exit()


if __name__ == "__main__":
    main()

