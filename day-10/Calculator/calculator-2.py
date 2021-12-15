from art import logo

def sum(a, b):
    return a + b

def substraction(a, b):
    return a- b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    "+": sum,
    "-": substraction, 
    "*": multiply,
    "/": divide, 
}
def calculator():
    print(logo)
    game_inProgress = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while game_inProgress is True:

        # First operation
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(num1, num2), 2)
        num1 = answer

        # End Game?
        user_response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:  ").lower()
        if user_response == "n":
            game_inProgress = False
            calculator()



