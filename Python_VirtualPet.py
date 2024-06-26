# Author: Nicole Brandenburg
# Date: May 2024

"""
This project is a Virtual Pet Dog. My inspiration for this project is the nano baby / pets that were popular
when I was a child. The user will have a pet dog to keep alive, healthy, and happy. After the pet is created,
the user will view an options menu to interact with their dog.

This Project Demonstrates:

    Flow Control:   Flow control is used throughout the project. One example is processing the Menu Options.
                    
    Functions:      Functions begin on line 59 of this file.
    
    Dictionaries:   The stats are stored in a dictionary in the Dog class in the the Dog.py file.
    
    Logging Module: A logging.critical statement is used to notify the user if the Dog.py class file is missing.
                    The logging.debug statements are used throughout to document user input and the start and end of
                    the program in a ProgramLog.txt file.
                    The logging.warning statements are used to document invalid input by the user.
                    
    Object-Oriented
    Programming:    A Dog class is stored in a separate file, Dog.py.

"""

import sys      # required to use sys.exit()
import logging  # required for logging debug and critical information


# Configure CRITICAL operations
logging.basicConfig(filename='ProgramLog.txt',
                    level=logging.CRITICAL,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# import Dog class from Dog.py
try:
    from Dog import *
    logging.debug("Dog.py class file loaded successfully.")
except:
    logging.critical("Missing Dog.py class file. The program will now exit.")
    print("Missing Dog.py class file. The program will now exit.")
    sys.exit()

#----------------------------------------------------------------------------------------------#

#   VARIABLES

keepPlaying = True  # continue game while True, initialized to True
choice = 0          # menu option as entered by user

#----------------------------------------------------------------------------------------------#

#   FUNCTIONS

# Welcome Statement
def welcome():
    # Print Welcome Statement
    print("Hello! Are you ready to meet your Virtual Dog?")    

# Options Menu: Returns Users Choice
def optionsMenu():
    print("\n" + "OPTIONS".center(50, '.') + "\n")
    print(f"   1. Start a New Day")
    print(f"   2. Feed {dog.name}")
    print(f"   3. Walk {dog.name}")
    print(f"   4. Train {dog.name}")
    print(f"   5. Pet {dog.name}")
    print(f"   6. View {dog.name}'s Stats")
    print( "   7. Get a New Dog")
    print( "   8. End Game")
    print(".".center(50, '.') + "\n")

# Start a New Day
def startNewDay():
    # Print Message to User 
    print("It's a New Day!")
    
    # Log to ProgramLog.txt
    logging.debug("Starting New Day")

    # Update Stats for a new day and display to user
    dog.setNewDayStats()
    dog.displayStats()

# Get a New Dog
def getNewDog():
    # Log to ProgramLog.txt
    logging.debug("Starting with a new dog.")
    
    # Print Message to User
    print("Are you sure you want to say goodbye to " + dog.name + " and get a new dog?")
    print("Enter 'y' for yes or 'n' for no.")
    newDog = input()
    
    # Log user input
    logging.debug("User entered: " + newDog)

    # Sanitize Input
    # Remove whitespace
    newDog.strip()
    
    # Make sure lower case of choice is the letter y or n
    while(newDog.lower() != 'y' and newDog.lower() != 'n'):
        # Log warning for invalid entry
        logging.warning("User did not enter a valid Menu choice. Prompting user again.")
        print("Please enter 'y' for yes or 'n' for no.")
        newDog = input()
        
        # Log user input
        logging.debug("User entered: " + newDog)

    # If User is sure they want a new dog, set sure to True
    if(newDog.lower() == 'y'):

        # Reset Stats
        dog.newDogStats()
        
        # Display Welcome Message and change Name
        welcome()
        dog.nameNewDog()
        
# End Game
def endGame():
    global keepPlaying
    keepPlaying = False
    
    # Print message to user 
    print("Thank you for playing!")
    
    # Log to ProgramLog.txt
    logging.debug("Exiting Program")

#----------------------------------------------------------------------------------------------#

# MAIN PROGRAM

# Log to ProgramLog.txt
logging.debug("Start of Program")

# Display Welcome Message
welcome()

# Create a new dog object and name the dog
dog = Dog()
dog.nameNewDog()
    
while(keepPlaying):    
    # Display Menu
    optionsMenu()

    # Request and recieve user input
    print("Enter selection: ")
    choice = input()

    # Log user input
    logging.debug("User entered Menu choice: " + choice)

    # Sanitize input
    # Remove whitespace
    choice = choice.strip()
    
    # Make sure input is a digit 1 or 2
    while(choice.isdecimal() == False or int(choice) < 1 or int(choice) > 8):
        
        # Log warning for invalid entry
        logging.warning("User did not enter a valid Menu choice. Prompting user again.")

        # Request new input from user
        print("Please enter a number between 1 and 8.")
        choice = input()

        # Log user input
        logging.debug("User entered Menu choice: " + choice)
      
    if(int(choice) == 1):   # New Day
        startNewDay()      
    elif(int(choice) == 2): # Feed Dog
        dog.feed()        
    elif(int(choice) == 3): # Walk Dog
        dog.walk()        
    elif(int(choice) == 4): # Train Dog
        dog.train()        
    elif(int(choice) == 5): # Pet Dog
        dog.pet()        
    elif(int(choice) == 6): # View Stats
        dog.displayStats()
    elif(int(choice) == 7): # New Dog
        getNewDog()
    elif(int(choice) == 8): # End Game
        endGame()        
