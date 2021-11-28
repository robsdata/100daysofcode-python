# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0

if size == "S":
    print("Your selection is SMALL")
    price += 15
elif size == "M":
    print("Your selection is MEDIUM")
    price += 20
elif size == "L":
    print("Your selection is LARGE")
    price += 20
else:
    print("Invalid")


if add_pepperoni == "Y" and size == "S":
    print("You added single extra peperoni to your pizza")
    price += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    print("You added extra peperoni to your pizza")
    price += 3
else:
    print("Invalid EXTRA PEPPERONI")

if extra_cheese == "Y":
    print("You added extra cheese to your pizza")
    price += 1
else:
    print("Invalid EXTRA CHEESE")

print(f"Your final bill is: ${price}")

