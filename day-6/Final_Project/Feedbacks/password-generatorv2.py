""""
From feedback:

I would guess that yours is the second one? Functionally, yes, they seem to be equivalent. I didn't notice anything that would make a different result. 

But if we're talking about computation and space complexity, only creating one list would be better. And while this is for a beginner,  one pattern I might start getting in the habit of is this:

Whenever you see yourself doing something like 
password = ""
for char in password_list:
    password += char

Instead I would use something like this:
password = "".join(password_list)

Behind the scenes, IIRC, joining something like this is faster than what would be needed to establish a variable and then add to it in a for loop.

"""


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_raw =[]

for letter in range(1, (nr_letters + 1)):
    password_raw += random.choice(letters)

for symbol in range(1, (nr_symbols + 1)):
    password_raw += random.choice(symbols)

for number in range(1, (nr_numbers + 1)):
    password_raw += random.choice(numbers)

random.shuffle(password_raw)
password = "".join(password_raw)


print(f"Your password is: {password}")