#Task 1
#create menu

def display_menu():
    """
    Displays a menu with numbered options.
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
    rightAlignment = "wildlife> species Cairns"
    print(f"{leftAlignment : <20}{ rightAlignment : >27}")

























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



def search_species(city):
    return [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]


def display_species(species_list):
    if not species_list:
        print("Species not found.")
    else:
        for species in species_list:
            Acceptedname=species["Species"]["AcceptedCommonName"]
            Status=species["Species"]["PestStatus"]
            print(f"Species: {Acceptedname}")
            print(f"Pest Status: {Status}")

def main():
    display_menu()

    while True:
        userInput = input("Wildlife>").strip().lower() 
        print(f"The option that you have chosen is, {userInput}!")
        
        if userInput == "help" or userInput ==  "Display help":
            display_menu()
        elif userInput == "exit" or userInput == "Exit the application":
            print("Exit the Application")
            breask
        elif userInput.startswith("species"):
            city = command.split()[1]
            species_list = search_species(city)
            display_species(species_list)
         else:
            print("Invalid command. Please try again or seek help.")

main()

































#Task 4
#function that:...
