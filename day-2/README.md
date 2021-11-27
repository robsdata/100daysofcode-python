# Day 2 - Understanding Data Types and How to Manipulate Strings
## Overview

### Objective

Learn about datatypes, numbers, operations, type conversion, f-strings.

### Project

- **Tip Calculator**: It says, welcome to the tip calculator user. It asks for the total bill that you need to pay. It asks you how many people do you want to split the bill between? What percentage tip would you like to give? It's going to calculate what each person should pay, taking into account all of these pieces of information that you've put in.

## Lesson Cheat Sheet

### Integers

Integers are whole numbers.

### Floating Point Numbers

Floats are numbers with decimal places. When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be a floating point number.

### Strings

A string is just a string of characters. It should be surrounded by double quotes.

### String Concatenation

You can add strings to string to create a new string. This is called concatenation.
It results in a new string.

### Escaping a String

Because the double quote is special, it denotes a string, if you want to use it in
a string, you need to escape it with a "\"

### F-Strings

You can insert a variable into a string using f-strings. The syntax is simple, just insert the variable in-between a set of curly braces {}.

### Converting Data Types

You can convert a variable from 1 data type to another. 

- Converting to float: float()
- Converting to int: int()
- Converting to string: str()

### Checking Data Types

You can use the type() function to check what is the data type of a particular  variable.

### Round

```python
print "%.2f" % (39.54484700000000)
```

```python
print("{:.2f}".format(39.54484700000000))
```

```python
print(f'{39.54484700000000:.2f}')
```