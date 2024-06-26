# INF360 - Programming in Python
# Nicole Brandenburg
# Final Project

# Dog Class File Dog.py for Final Project

import logging # required for logging debug and critical information

class Dog:
    
    def __init__(self):
        self.name = ""
        self.days = 0                                  # dog's age in days, initialized to 0
        self.hunger = "Very hungry"                    # hunger status, initialized to "Very hungry"
        self.hungerScore = 0                           # hungerScore, initialized to 0
        self.health = "Very healthy"                   # health, initialized to "Very healthy"
        self.healthScore = 100                         # healthScore out of 100, initialized to 100
        self.skill = 0                                 # points earned by training, initialized to 0
        self.happiness = "Happy"                       # happiness level, initialized to "Happy"
        self.happinessScore = 50                       # happinessScore out of 100, initialized to 50
        self.relationship = "Not sure about you, yet"  # dog's relationship with owner, initialized to "Not sure about you, yet"
        self.relationshipScore = 50                    # relationshipScore, initialized to 50
        self.stats = {}                                # Stats Dictionary, initially empty

    def nameNewDog(self):
        # Request user input
        print("What is your puppy's name?")
        name = input()

        # Log user input
        logging.debug("User entered: " + name + " as dog name.")

        # Sanitize input
        # Remove outer whitespace
        name.strip()

        # Make sure name is alphanumeric
        while(name.isalnum() == False):            
            # Log warning for invalid entry
            logging.warning("User did not enter a valid name. Prompting user again.")
        
            print("Your dog's name must contain letters or numbers. Please try again.")
            name = input()        

            # Log user input
            logging.debug("User entered: " + name + " as dog name.")

        # Set dog's name
        self.name = name
        
        print("\nYour Virtual Puppy is named " + name + "!")
        
    def setNewDayStats(self):
        # age increases by 1 day
        self.days += 1

        # hungerScore reset to 0
        self.hungerScore = 0

        # healthScore, happinessScore, relationshipScore all decrease by 5
        self.healthScore -= 5
        self.happinessScore -= 5
        self.relationshipScore -= 5

    def feed(self):
        # Display options to feed dog
        print("\n" + "OPTIONS".center(50, '.') + "\n")
        print("   1. Feed your dog a Meal")
        print("   2. Feed your dog a Treat")
        print(".".center(50, '.') + "\n")
        
        # Request and receive user input
        print("What would you like to feed " + self.name + "?")
        foodChoice = input()

        # Log user input
        logging.debug("User entered Food choice: " + foodChoice)

        # Sanitize input
        # Remove whitespace
        foodChoice = foodChoice.strip()
        
        # Make sure input is a digit 1 or 2
        while(foodChoice.isdecimal() == False or int(foodChoice) < 1 or int(foodChoice) > 2):            
            # Log warning for invalid entry
            logging.warning("User did not enter a valid Food choice. Prompting user again.")
            
            # Request new input
            print("Please enter 1 or 2")
            foodChoice = input()
            
            # Log user input
            logging.debug("User entered Food choice: " + foodChoice)  

        # Set previous hungerScore to compare
        prevHungerScore = self.hungerScore
        
        # Update hungerScore based on user choice
        if(int(foodChoice) == 1):
            # Meal increases hungerScore by 3
            print(self.name + " ate a bowl of dog food.\n")
            self.hungerScore += 3
        elif(int(foodChoice) == 2):
            # Treat increases hungerScore by 1
            print(self.name + " ate a treat.\n")
            self.hungerScore += 1

        # Display message
        print(self.name + "'s hunger score improved from " + str(prevHungerScore) + " to " + str(self.hungerScore))

        # Log updated hungerScore
        logging.debug("hungerScore improved from " + str(prevHungerScore) + " to " + str(self.hungerScore))

    def walk(self):
        # Walks improve health and happiness
        
        # Set previous healthScore for comparison
        prevHealthScore = self.healthScore
        
        # One walk increases dog's health by 15 points
        self.healthScore += 15

        # Set previous happinessScore for comparison
        prevHappinessScore = self.happinessScore

        # One walk increases dog's happinessScore by 15 points
        self.happinessScore += 15

        # Display message
        print(self.name + " enjoyed their walk.")
        print(self.name + "'s health improved from " + str(prevHealthScore) + " to " + str(self.healthScore))
        print(self.name + "'s happiness improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))

        # Log updated healthScore and happinessScore
        logging.debug("healthScore improved from " + str(prevHealthScore) + " to " + str(self.healthScore))
        logging.debug("happinessScore improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))

    def train(self):
        # Fetch, sit, and stay improve skill level. Fetch also improves happiness.
        
        # Display options
        print("\n" + "OPTIONS".center(50, '.') + "\n")
        print("   1. Play Fetch")
        print("   2. Practice 'Sit'")
        print("   3. Practice 'Stay'")
        print(".".center(50, '.') + "\n")

        # Request and receive user input
        print("How would you like to train " + self.name + "?")
        trainingChoice = input()

        # Log user input
        logging.debug("User entered Training choice: " + trainingChoice) 

        # Sanitize input
        # Remove whitespace
        trainingChoice = trainingChoice.strip()
        
        # Make sure input is a digit 1 or 2
        while(trainingChoice.isdecimal() == False or int(trainingChoice) < 1 or int(trainingChoice) > 3):
            # Log warning for invalid entry
            logging.warning("User did not enter a valid Training choice. Prompting user again.")

            # Request new input
            print("Please enter a number between 1 and 3.")
            trainingChoice = input()

            # Log user input
            logging.debug("User entered Training choice: " + trainingChoice)

        # Set previous levels for comparison
        prevSkill = self.skill
        prevHappinessScore = self.happinessScore

        if(int(trainingChoice) == 1):
            # Playing fetch increases skill by 1
            self.skill += 1

            # Playing fetch increases happiness by 10
            self.happinessScore += 10

            # Display message
            print(self.name + " loves playing fetch.")
            print(self.name + "'s skill improved from " + str(prevSkill) + " to " + str(self.skill))
            print(self.name + "'s happiness improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))

            # Log updated skill and happinessScore
            logging.debug("skill improved from " + str(prevSkill) + " to " + str(self.skill))
            logging.debug("happinessScore improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))
            
        elif(int(trainingChoice) == 2):
            # Practicing 'Sit' increases skill by 5
            self.skill += 5

            # Display message
            print(self.name + " is learning to sit.")
            print(self.name + "'s skill improved from " + str(prevSkill) + " to " + str(self.skill))

            # Log updated skill
            logging.debug("skill improved from " + str(prevSkill) + " to " + str(self.skill))

        elif(int(trainingChoice) == 3):
            # Practicing 'Stay' increases skill by 8
            self.skill += 8

            # Display message
            print(self.name + " is learning to stay.")
            print(self.name + "'s skill improved from " + str(prevSkill) + " to " + str(self.skill))

            # Log updated skill
            logging.debug("skill improved from " + str(prevSkill) + " to " + str(self.skill))

        # Make sure input is 1, 2, or 3
        else:
            print("Please enter 1, 2, or 3.")
            trainingChoice = input()

    def pet(self):
        # Improves happiness and relationship scores.

        # Set previous levels for comparison
        prevHappinessScore = self.happinessScore
        prevRelationshipScore = self.relationshipScore

        # Petting dog increases happinessScore by 10
        self.happinessScore += 10

        # Petting dog increases relationshipScore by 10
        self.relationshipScore += 10

        # Display message
        print(self.name + "'s happiness improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))
        print(self.name + "'s relationship with you improved from " + str(prevRelationshipScore) + " to " + str(self.relationshipScore))

        # Log updated happinessScore and relationshipScore
        logging.debug("happinessScore improved from " + str(prevHappinessScore) + " to " + str(self.happinessScore))
        logging.debug("relationshipScore improved from " + str(prevRelationshipScore) + " to " + str(self.relationshipScore))
        
    def newDogStats(self):
        # Reset stats to beginning values
        self.days = 0
        self.hunger = "Very hungry"
        self.hungerScore = 0
        self.health = "Very Healthy"
        self.healthScore = 100
        self.skill = 0
        self.happiness = "Happy"
        self.happinessScore = 50
        self.relationship = "Not sure about you, yet"
        self.relationshipScore = 50

    def updateHunger(self):        
        # Update hunger stat based on hungerScore
        # hungerScore range is 0 - 10+
        
        # A hungerScore of 0 is 'Very hungry!'
        if(self.hungerScore == 0):
            self.hunger = "Very hungry!"
        # A hungerScore of 1 - 2 is 'Still hungry'
        elif(self.hungerScore <= 2):
            self.hunger = "Still hungry"
        # A hungerScore of 3 - 5 is 'A little hungry'
        elif(self.hungerScore <= 5):
            self.hunger = "A little hungry"
        # A hungerScore of 5 or greater is 'Full!'
        else:
            self.hunger = "Full!"

    def updateHealth(self):
        # Update health stat based on healthScore
        # healthScore range is 0 - 100+

        # A healthScore of 0 is 'Very poor health!'
        if(self.healthScore == 0):
            self.health = "Very poor health!"
        # A healthScore of 1 - 49 is 'Poor health'
        elif(self.healthScore < 50):
            self.health = "Poor health"
        # A healthScore of 50 - 74 is 'Healthy' 
        elif(self.healthScore < 75):
            self.health = "Healthy"
        # A healthScore of 75 or greater is 'Very healthy!'
        else:
            self.health = "Very healthy!"

    def updateHappiness(self):
        # Update happiness stat based on happinessScore
        # happinessScore range is 0 - 100+

        # A happinessScore of 0 is 'Sad!'
        if(self.happinessScore == 0):
            self.happiness = "Sad!"
        # A happinessScore of 1 - 50 is 'Happy'
        elif(self.happinessScore <= 50):
            self.happiness = "Happy"
        # A happinessScore of 51 - 75 is 'Very happy'
        elif(self.happinessScore <= 75):
            self.happiness = "Very happy"
        # A happinessScore of 76 or greater is 'The happiest dog!'
        else:
            self.happiness = "The happiest dog!"

    def updateRelationship(self):
        # Update relationship stat based on relationshipScore
        # relationshipScore range is 0 - 100

        # A relationshipScore of 0 is 'Doesn't like you!'
        if(self.relationshipScore == 0):
            self.relationship = "Doesn't like you!"
        # A relationshipScore of 1 - 50 is 'Not sure about you, yet'
        elif(self.relationshipScore <= 50):
            self.relationship = "Not sure about you, yet"
        # A relationshipScore of 51 - 75 is 'Likes you'
        elif(self.relationshipScore <= 75):
            self.relationship = "Likes you"
        # A relationshipScore of 76 or greater is 'Loves you!'
        else:
            self.relationship = "Loves you!"

    def fillStats(self):
        # Update stats
        self.updateHunger()
        self.updateHealth()
        self.updateHappiness()
        self.updateRelationship()
        
        # Fill Stats Dictionary
        self.stats = {
            "Name": self.name,
            "Age": str(self.days) + " Days",
            "Hunger": str(self.hungerScore) + " - " + self.hunger,
            "Health": str(self.healthScore) + " - " + self.health,
            "Skill": str(self.skill) + " Points",
            "Happiness": str(self.happinessScore) + " - " + self.happiness,
            "Relationship": str(self.relationshipScore) + " - " + self.relationship
            }

    def displayStats(self):        
        # Fill Stats Dictionary
        self.fillStats()

        # Display Stats to User
        print("\n" + "STATS".center(50, '.') + "\n")
        for k, v in self.stats.items():
            print("   " + str(k) + ': ' + str(v))
        print(".".center(50, '.') + "\n")
