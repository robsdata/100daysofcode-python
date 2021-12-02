# Day 6 - Python Functions & Karel

## Overview

### Objective

Code blocks and indentation functions and while loop

### Project

A code that's required to instruct our little robot to be able to complete any randomly generated maze.

# Lesson Cheat Sheet

## While Loop

This is a loop that will keep repeating itself until the while condition becomes false.

## Infinite Loops

Sometimes, the condition you are checking to see if the loop should continue never becomes false. In this case, the loop will continue for eternity (or until your computer stops it). This is more common with while loops.

## Creating Functions

This is the basic syntax for a function in Python. It allows you to give a set of instructions a name, so  you can trigger it multiple times without having to re-write or copy-paste it. The contents of the function must be indented to signal that it's inside. 

```python
def my_function():
	print("Hello")
	name = input("Your name:")
	print("Hello")
```

## Calling Functions

You activate the function by calling it. This is simply done by writing the name of the function followed by a set of round brackets. This allows you to determine when to trigger the function and how many times.

```python
my_function()
my_function()
#The function my_function
#will run twice.
```

[https://reeborg.ca/index_en.html](https://reeborg.ca/index_en.html)