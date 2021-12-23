# Initial commit

from coffee_machine_items import menu, resources

# TODO: Check transaccion successful?
# TODO: Make Coffee ☕



# TODO: Print Report
def view_report(money):
    """
    It receives current amount, and prints report
    """
    money = 0.0
    for item in resources:
        print(f"{item} : {resources[item]}")
    print(f"money: ${money}")


# TODO: Process coins
def coins_to_user_total(quarters, dimes, nickles, pennies):
    """
    quarters, dimes, nickles, pennies and returns total
    """
    total = 0
    for i in range(quarters):
        total += 0.25
    for i in range(dimes):
        total += 0.10
    for i in range(nickles):
        total += 0.05
    for i in range(pennies):
        total += 0.01
    return round(total, 2)

def user_insert_coin():
    """
    Returns user total (float) from input quarters, dimes, nickles, pennies 
    """
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input("how many pennies?: "))

    user_total = coins_to_user_total(quarters, dimes, nickles, pennies)

    return user_total




# TODO: Check resources sufficient?


machine_resources = resources
coffe_menu_list = [i for i in menu]
ready_to_charge = False
ready_to_deliver = False
incorrect_value = False
not_ingredients = False
refund_no_money = False

# print(machine_resources)
# print(coffe_menu_list)
# print(menu['espresso'])
# print(menu['espresso']['ingredients'])
# print(menu['espresso']['cost'])
# print(resources)

# user_selection = 'espresso'


user_selection = input('What would you like? (espresso/latte/cappuccino): ').lower()

if user_selection in coffe_menu_list: 
    ready_to_charge = True
    cost = menu[user_selection]['cost']  
    for recipe_item in menu[user_selection]['ingredients']:
        # print(recipe_item)
        # print(machine_resources[recipe_item])
        quantity_menu = menu[user_selection]['ingredients'][recipe_item]
        quantity_machine = machine_resources[recipe_item]
        # print(f"QMenu: {quantity_menu}")
        # print(f"QMachine resource: {quantity_machine}")

        if quantity_machine >= quantity_menu:
            # print(f"Before: {recipe_item}, machine resources {machine_resources}")
            machine_resources[recipe_item] -= menu[user_selection]['ingredients'][recipe_item]
            # print(f"After: {recipe_item}, machine resources {machine_resources}")
        else:
            ready_to_charge = False
            not_ingredients = True
            print("Not enough engridients")
    print(f"Success, ready_to_charge is {ready_to_charge}")
else:
    incorrect_value = True
    print("Incorrect value")


# ready_to_charge = True
# user_selection = 'espresso'
# cost = menu[user_selection]['cost']
# change = 0 
# total_user = float(input("Amount: "))



if ready_to_charge is True:
    total_user = user_insert_coin()
    if total_user == cost:
        ready_to_deliver = True
        
    elif total_user > cost:
        change = round((total_user - cost), 2)
        print(f'Here is ${change} in change.')
        ready_to_deliver = True
    else:
        refund_no_money = True
        print('Sorry that\'s not enough money. Money refunded.')

if ready_to_deliver is True:
    print(f"Here is your {user_selection} ☕️. Enjoy!")




# if user_selection == 'espresso':
#     print(f'{user_selection} selected')
# elif user_selection == 'latte':
#     print(f'{user_selection} selected')
# elif user_selection == 'capuccino':
#     print(f'{user_selection} selected')
# elif user_selection == 'report':
#     print(f'{user_selection} selected')
# else:
#     print('Incorrect entry')