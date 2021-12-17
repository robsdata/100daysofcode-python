from games import blackjack

keep_playing = True

while keep_playing == True:
    blackjack()
    should_keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if should_keep_playing == "n":
        keep_playing = False