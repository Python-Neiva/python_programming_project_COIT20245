# COIT20245_programming_project
Python repo

- Hamza Arif:12244212
- Parul: 12261175
- Sebastian Romero:12242040

Open a terminal or command prompt and navigate to the directory containing main.py. Then, type the following command and press Enter: python main.py

# Executive Summary
This document outlines the development of a Python program that retrieves and analyzes data about animal observations in Queensland, Australia. Users can interact with the program to find:

Lists of species in a specified city
Lists of animal sightings for a particular species in a city
Venomous species in an area
The program communicates with external web services:

Nominatim geocoding service: Translates city names into GPS coordinates.
Queensland Wildlife Data API: Provides information on species and sightings.

## Key functionalities implemented:

User interface with a menu for selecting options.
Functions to retrieve species lists and sighting data from the Wildlife Data API based on city and species.
Ability to filter venomous species.
Function to sort sightings by date (ascending order).

## Development Approach:

Iterative development process over three weeks.
Regular testing using assert statements within the code.
Version control with a private Git repository.

## Limitations:

Relies on the availability and functionality of external web services.
Fixed search radius of 100 kilometres.
There is no user customization for the search radius.

## Conclusion:

This project provided valuable experience building a Python application that interacts with web services, processes user input, and displays data. The development process emphasized a disciplined and organized approach through iterative development, testing, and version control.
