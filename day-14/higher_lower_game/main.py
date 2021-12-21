from game_data import data
from art import vs, logo
import random

def game_parameters():
    selection_index = random.randint(0, 49)
    parameters = data[selection_index]
    return parameters


game_inprogress = True
correct_guesses = 0
correct_selection = False
user_selection = ''
pc_selection = ''
user_selection_follower_count = 0
pc_selection_follower_count = 0


print(logo)


while game_inprogress == True:

    a_selection = game_parameters()
    b_selection = game_parameters()
    while b_selection == a_selection:
        b_selection = game_parameters()

    print(f"Compare A: {a_selection['name']}, a/an {a_selection['description']}, from {a_selection['country']} ")
    # print(f"Psssst: Followers = {a_selection['follower_count']}")
    print(vs)
    print(f"Compare B: {b_selection['name']}, a/an {b_selection['description']}, from {b_selection['country']} ")
    # print(f"Psssst: Followers = {b_selection['follower_count']}")

    user_option_entry = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_option_entry == 'a':
        user_selection = a_selection['follower_count']
        pc_selection = b_selection['follower_count']
        correct_selection = True
        # print("a selected")
        # print(f"selection is: {user_selection}")
    elif user_option_entry == 'b':
        user_selection = b_selection['follower_count']
        pc_selection = a_selection['follower_count']
        correct_selection = True
        # print("b selected")
        # print(f"selection is: {user_selection}")
    else:
        print(f"Sorry, that's wrong. Final score: {correct_guesses}")
        game_inprogress = False

    if game_inprogress == True:
        if user_selection > pc_selection:
            correct_guesses += 1
            print(f"\nYou're right! Current score: {correct_guesses}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {correct_guesses}")
            game_inprogress = False