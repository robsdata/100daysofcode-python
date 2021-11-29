import random
start = input("Heads or tails generator: (type \"Y\" to flip the coin)\n---->" ).lower()

if start == "y":
    coin = random.randint(0,1)
    
    if coin == 0:
        print("Tails")
    else: 
        print("Head")

else:
    print("Vuelve a correr el programa.")