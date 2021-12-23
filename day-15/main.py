

from coffee_machine_items import menu, resources

def view_report(money):
    """
    It receives current amount, and prints report
    """
    for item in resources:
        print(f"{item} : {resources[item]}")
    print(f"money: ${money}")

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

machine_balance = 0
machine_resources = resources
coffe_menu_list = [i for i in menu]
ready_to_charge = False
ready_to_deliver = False
incorrect_value = False
not_ingredients = False
refund_no_money = False
coffee_machine_on = True

while coffee_machine_on is True:
    user_selection = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_selection in coffe_menu_list: 
        ready_to_charge = True
        cost = menu[user_selection]['cost']  
        for recipe_item in menu[user_selection]['ingredients']:
            quantity_menu = menu[user_selection]['ingredients'][recipe_item]
            quantity_machine = machine_resources[recipe_item]
            if quantity_machine >= quantity_menu:
                machine_resources[recipe_item] -= menu[user_selection]['ingredients'][recipe_item]
            else:
                ready_to_charge = False
                not_ingredients = True
                coffee_machine_on = False
                ready_to_deliver = False
                print("Not enough engridients")
    elif user_selection == 'report':
        view_report(machine_balance)
        ready_to_charge = False
        ready_to_deliver = False
    else:
        incorrect_value = True
        print("Incorrect value")


    if ready_to_charge is True:
        total_user = user_insert_coin()
        if total_user == cost:
            ready_to_deliver = True
            print(f"MB Before: {machine_balance}")
            machine_balance += cost
            print(f"MB After: {machine_balance}")
        elif total_user > cost:
            change = round((total_user - cost), 2)
            print(f'Here is ${change} in change.')
            ready_to_deliver = True
            print(f"MB Before: {machine_balance}")
            machine_balance += cost
            print(f"MB After: {machine_balance}")
        else:
            refund_no_money = True
            print('Sorry that\'s not enough money. Money refunded.')

    if ready_to_deliver is True:
        print(f"Here is your {user_selection} ☕️. Enjoy!")

