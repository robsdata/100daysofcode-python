# Day 5 - Python Loops

## Overview

### Objective

Python Loops

### Project

- **Password Generator:**

It asks how many letters would you like in your password? How many symbols would you like? And how many numbers?

# Lesson Cheat Sheet

## For Loop

For loops give you more control than while loops. You can loop through anything that is iterable. e.g. a range, a list, a dictionary or tuple

## Range

Often you will want to generate a range of numbers. You can specify the start, end and step.
Start is included, but end is excluded: start >= range < end

## Importing

Some modules are pre-installed with python e.g. random/datetime Other modules need to be installed from [pypi.org](http://pypi.org/)

## random.**randint**(*a*, *b*)

Return a random integer *N* such that `a <= N <= b`. Alias for `randrange(a, b+1)`.

## **random.choice(*seq*)**

Return a random element from the non-empty sequence *seq*. If *seq* is empty, raises `[IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)`.

## **random.shuffle(*x*[, *random*])**

Shuffle the sequence *x* in place.