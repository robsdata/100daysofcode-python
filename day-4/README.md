# Day 4 - Randomization and Python Lists

## Overview

### Objective

Randomization and python lists.

### Project

Rock-paper-scissors game.

# Lesson Cheat Sheet

### import random

### randrange(start, stop, step)

Returns a randomly selected integer from `range(start, stop, step)`. This raises a `ValueError` if `start` > `stop`.

### randint(a, b)

Returns a random integer between **a** and **b** (both inclusive). This also raises a `ValueError` if `a` > `b`.

### random.**random**()

Returns the next random floating point number between [0.0 to 1.0)

### Lists

A list is a data structure. It's a way of organizing data in Python

[5. Data Structures - Python 3.10.0 documentation](https://docs.python.org/3/tutorial/datastructures.html)

### Adding Lists Together

You can extend a list with another list by using the extend keyword, or the + symbol. Adding an Item to a List If you just want to add a single item to a list, you need to use the .append() method. 

### List Index

To get hold of a particular item from a list you can use its index number. This number can also be negative, if you want to start counting from the end of the list.

### List Slicing

Using the list index and the colon symbol you can slice up a list to get only the portion you want. Start is included, but end is not.