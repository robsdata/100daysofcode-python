import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.



options = [rock, paper, scissors]
user_selection = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))

user_print_selection = options[user_selection]
computer_selection = random.randint(0, 2)
computer_print_selection = options[computer_selection]


# Rock(0) wins against scissors (2).
# Paper(1) wins against rock (0).
# Scissors(2) win against paper (1).

#User vs PC - Evaluar el resultado del usuario vs el de la pc

#Rock
if user_selection == 0:
    print(user_print_selection)
    #draw
    if computer_selection == 0:
        print("Computer Choose")
        print(computer_print_selection)
        print("It's a draw")
    #win 
    elif computer_selection == 2:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Win!")
    #lose
    else:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Loose!")


#Paper
if user_selection == 1:
    print(user_print_selection)
    #draw
    if computer_selection == 1:
        print("Computer Choose")
        print(computer_print_selection)
        print("It's a draw")
    #win 
    elif computer_selection == 0:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Win!")
    #lose
    else:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Loose!")

#Scissors
if user_selection == 2:
    print(user_print_selection)
    #draw
    if computer_selection == 2:
        print("Computer Choose")
        print(computer_print_selection)
        print("It's a draw")
    #win 
    elif computer_selection == 1:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Win!")
    #lose
    else:
        print("Computer Choose")
        print(computer_print_selection)
        print("You Loose!")


