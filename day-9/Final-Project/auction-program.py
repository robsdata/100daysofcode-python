
from art import logo


print(logo)
game_in_progress = True
bid_list = []
max_bid = 0
user_max_bid = ""


while game_in_progress == True:
    new_bid = {}
    
    bid_owner = input("What is your name?: ")
    bid_amount = float(input("What is your bid?: $"))

    new_bid['name'] = bid_owner
    new_bid['amount'] = bid_amount

    bid_list.append(new_bid)

    print(f"Current bid list is: \n{bid_list}")

    user_game_decision = input("Are there any other bidders? Type 'yes or 'no'\n").lower()

    if user_game_decision == "no":
        game_in_progress = False


#Winner

for item in bid_list:
  if item["amount"] > max_bid:
    max_bid = item["amount"]
    user_max_bid = item['name']

print(f"The winner is {user_max_bid} with a bid of ${max_bid}")

    
