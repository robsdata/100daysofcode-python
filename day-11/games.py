import random
from art import logo

def final_message(final_user_selection, final_user_selection_total, final_pc_selection, final_pc_selection_total):
    print(f"Your final hand: {final_user_selection}, final score: {final_user_selection_total}")
    print(f"Computer's final hand: {final_pc_selection}, final score: {final_pc_selection_total}")

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Initial Game Setup
    user_selection = [random.choice(cards) for card in range(2)]
    user_selection_total = sum(user_selection)
    pc_selection = [random.choice(cards) for card in range(2)]
    pc_selection_total = sum(pc_selection)
    blackjack = 21
    blackjack_in_progress = True
    user_went_over = False
    user_blackjack = False
    pc_blackjack = False
    draw = False


    #Game Starts
    print(logo)
    while blackjack_in_progress == True:
        # user and pc gets blackjack draw
        if user_selection_total == blackjack and pc_selection_total == blackjack:
            pc_blackjack = True
            user_blackjack = True
            blackjack_in_progress = False

        # user gets blackjack win
        elif user_selection_total == blackjack:
            user_blackjack = True
            blackjack_in_progress = False

        elif pc_selection_total == blackjack:
            pc_blackjack = True

        # user can decide to pick another card or stay
        elif user_selection_total <= blackjack:
            print(f"Your cards: {user_selection}, current score: {user_selection_total}")
            print(f"Computer's first card: {pc_selection[0]}")
            other_card_user_selection = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            # User selects YES
            if other_card_user_selection == "y":
                user_selection.append(random.choice(cards))
                user_selection_total = sum(user_selection)
            
            # User selects NO
            elif other_card_user_selection == "n":
                blackjack_in_progress = False

        else:
            #Is there any As?
            for i in range(len(user_selection)):
                # print(f"Esta es la [ {i} ] vuelta, accesamos {cards[i]}")
                if user_selection[i] == 11:
                    user_selection[i] = 1 
                    user_selection_total = sum(user_selection)
            # user selection sum is more than 21 looses       
            if user_selection_total > blackjack:
                # print(f"Your cards: {user_selection}, current score: {user_selection_total}, you loose")
                blackjack_in_progress = False
                user_went_over = True

    if pc_blackjack is not True:
        while pc_selection_total < blackjack:
            pc_selection.append(random.choice(cards))
            pc_selection_total = sum(pc_selection)
        pc_selection.pop()
        pc_selection_total = sum(pc_selection)


    if user_went_over == True:
        final_message(user_selection, user_selection_total, pc_selection, pc_selection_total)
        print("You loose")
                
    elif pc_selection_total == user_selection_total:
        final_message(user_selection, user_selection_total, pc_selection, pc_selection_total)
        print("Draw")

    elif pc_selection_total > user_selection_total:
        final_message(user_selection, user_selection_total, pc_selection, pc_selection_total)
        print("PC Wins")

    else:
        final_message(user_selection, user_selection_total, pc_selection, pc_selection_total)
        print("User Wins") 
