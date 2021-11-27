
""""

num_char = len(input("What's your name? "))
print("Your name has " + num_char + " characters")

TypeError: can only concatenate str (not "int") to str

To check the data type we're working with, we could use the function 

type()

Yill check whatever you put between the parentheses and give you the type of data that it is. 

You can use the type function to investigate the data type you're working with and you can use functions like string, int, or float to convert to that data type.

"""

#Work around



num_char = len(input("What's your name? "))
new_num_char = str(num_char)

print("Your name has " + num_char + " characters")



