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


letters_list_lenght = len(letters) - 1
numbers_list_lenght = len(numbers) - 1
symbols_list_lenght = len(symbols) - 1

pwd_letters = []
pwd_symbol = []
pwd_numbers = []


for letter in range(0, nr_letters):
    pwd_letters.append(letters[random.randint(0, letters_list_lenght)])

for symbol in range(0, nr_symbols):
    pwd_symbol.append( symbols[random.randint(0, symbols_list_lenght)])

for number in range(0, nr_numbers):
    pwd_numbers.append(numbers[random.randint(0, numbers_list_lenght)])


password_raw = pwd_letters + pwd_numbers + pwd_symbol
random.shuffle(password_raw)


password = ""

for password_list_item in range(0, len(password_raw)):
    password += password_raw[password_list_item]



print(f"Your passwrd is {password}")
