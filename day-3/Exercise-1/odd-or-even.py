"""
Write a program that works out whether if a given number is an odd or even number.

"""

number = int(input("Enter the number to evaluate, this program tells if the number is odd or even: \n"))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")