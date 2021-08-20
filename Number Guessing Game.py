# Import random module
import random

# Number of guesses is 3
guesses = 3

# Getting a random number between and including 1 and 10
number = random.randint(1,10)

# Some basic print statements
print("Welcome to guess the number")
print("You have to guess a number from 1-10")
print("You have 3 guesses")

# While the guesses is greater than 0, repeat the code below.
while guesses >0:
    choice = int(input("Enter your guess (1-10): ")) # Getting the player input
    if choice == number: # If the player's choice is equal to the number
        print("You WIN!! The number was ",number) # Printing a win message and the number
        quit() # exit the programme
    elif choice < number: # If the player's input is smaller than the number, run the code below.
        guesses -=1 # Guesses minus 1, Player has one less guess.
        print("Your choice is smaller than the number. You have",guesses,"more guesses") # Giving a hint that the player's choice is smaller than the number
        
    elif choice > number: # If the player's choice is greater than the number, run the code below.
        guesses -=1 # Guesses minus 1, Player has one less guess.
        print("Your choice is bigger than the number. You have",guesses,"more guesses") # Giving a hint that the player's choice is bigger than the number

# When the number of guesses is 0, the code below only will be carried out as the player would have run out of guesses.
print("You lost!! The number is",number)# Printing a lose message and the number
