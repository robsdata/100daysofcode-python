import random
from art import logo

def lifes_level_selection():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "hard":
        lifes = 5
        print(f"Assigning {lifes} lifes")
        correct_level_selection = True
    elif level == "easy":
        lifes = 10
        print(f"Assigning {lifes} lifes")
        correct_level_selection = True
    else:
        lifes_level_selection()

    return lifes

def guess_game(level_selection):
    lifes = level_selection
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {number}")
    while lifes > 0:
        print(f"---You have {lifes} lifes---")
        user_selection = int(input("Make a guess: "))
        if user_selection == number:
            lifes = 0
            print(f"You got it! The answer was {number}.")
        elif user_selection > number:
            lifes -= 1
            print(f"Too high, lifes: {lifes}.")
        elif user_selection < number:
            lifes -= 1
            print(f"Too low, lifes: {lifes}")
    
    should_continue = input("Should we continue playing (y/n)? \n").lower()
    if should_continue == "y":
        guess_game(level_selection)
    else:
        return print("Good bye!")

guess_game(lifes_level_selection())

    