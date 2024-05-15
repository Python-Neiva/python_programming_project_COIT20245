from nomination import gps_coordinate

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










 





























#Task 3
#function that:...

def display_species(specieList):
    print("Species found:")
    for species in specieList:
        acceptedName = species['Species']['AcceptedCommonName']
        pestStatus = species['Species']['PestStatus']
        print(f"Common Name: {acceptedName}, Pest Status: {pestStatus}")




#Task 4
def gps(city):
    # Stub implementation
   # return {"latitude": -27.4689682, "longitude": 153.0234991}
    coordinate = gps_coordinate(city)
    if coordinate:
       return coordinate
    else:
       return None
    
def search_species(city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of species for any city
   # coordinate = gps(city)
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil", "TaxonID": 1039}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous", "TaxonID": 1234}}
    ]

def assert_gps_function():
    assert gps("Brisbane") == {"latitude": -27.4689682, "longitude": 153.0234991}

def search_sightings(taxonid, city):
    # Stub implementation, to be replaced with actual logic later
    # For now, return a predefined list of sightings for any species and city
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_species(specieList):
    print("Species found:")
    for species in specieList:
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
    
def filter_venomous(speciesList):
    """
    Function to filter out non-venomous species from a list.
    """
    return [species for species in speciesList if species["Species"]["PestStatus"] == "Venomous"]

def assert_filter_venomous():
    assert filter_venomous([{"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}}]) == []
    assert filter_venomous([{"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}]) == [{"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}]
    assert filter_venomous([]) == []

#assert filter_venomous([]) == []
#assert filter_venomous([{"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}}]) == []
#assert filter_venomous([{"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}]) == [{"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}]











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
            print("Exiting Application")
            exit()

        if userInput.startswith("species"):
        # Get the city from the command
            if len(userInput.split()) >= 2 and userInput.split()[1] == "venomous":
                city = userInput.split()[1]
                speciesList = search_species(city)
                venomousSpeciesList = filter_venomous(speciesList)
                display_species(venomousSpeciesList)
            elif len(userInput.split()) >= 2 and userInput.split()[1] is not None:
                city = userInput.split()[1]
                speciesList = search_species(city)
                display_species(speciesList)
            else:
                print("Invalid command. Please use 'species <city>' or 'species <city> venomous'.")

        if userInput.startswith("sightings"):
            # Extract species and city from the command
            specieCityData = userInput.split()
            # Validate that the user input includes city and sightings
            if len(specieCityData) > 2:
                species, city = specieCityData[1], specieCityData[2]
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


if __name__ == "__main__":
    main()



