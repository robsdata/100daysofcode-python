import random

# converting string1 into a list of strings
# string1=string1.split()

list_names = input("Type de names here: \n").split(", ")
selected_name = list_names[random.randint(0, len(list_names)-1)]

print(f"{selected_name} is going to buy the meal today!")

