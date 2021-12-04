# Day 7 - Hangman

## Overview

### Project

- **Hangman**: Hangman or the code equivalent of this game. So the way the game works is you have to guess a word and for every wrong letter you submit, you end up taking a life away from this little man. And of course, the longer it takes you to get to the word, the more you put your little man in danger.

# Lesson Cheat Sheet


## Flow Chart
<img width="588" alt="flowchart" src="https://user-images.githubusercontent.com/62405434/144692615-52c150ca-5f2c-4f4d-8677-ef2a5f1f61a8.png">

## Python Lists

[Python List Comprehension](https://www.programiz.com/python-programming/list-comprehension)

## **List Comprehension**

It can identify when it receives a string or a tuple and work on it like a list.

**Syntax**

```python
[expression for item in list]
```

List comprehensions can utilize conditional statement to modify existing list (or other tuples). We will create list that uses mathematical operators, integers, and range().

**Code**

```python
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
```

**Output**

```python
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## FOR and IN

Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- `for **var** in **list**` -- is an easy way to look at each element in a list (or other collection). Do not add or remove from the list during iteration.

```python
  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum  ## 30

```

If you know what sort of thing is in the list, use a variable name in the loop that captures that information such as "num", or "name", or "url". Since Python code does not have other syntax to remind you of types, your variable names are a key way for you to keep straight what is going on.

The *in* construct on its own is an easy way to test if an element appears in a list (or other collection) -- **`value** in **collection**` -- tests if the value is in the collection, returning True/False.

```python
  list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print 'yay'
```

**The for/in constructs are very commonly used in Python code and work on data types other than list, so you should just memorize their syntax.** You may have habits from other languages where you start manually iterating over a collection, where in Python you should just use for/in.

You can also use for/in to work on a string. The string acts like a list of its chars, so `for ch in s: print ch` prints all the chars in a string.

## Python import Statement

Python **`import`** statement enables the user to import particular modules in the corresponding program.

It resembles the #include header_file in C/C++.

As soon as the interpreter encounters the import statement in a particular code, it searches for the same in the local scope and imports the module, if present in the search path.

It searches for a particular module in its built-in modules section at first. If it’s not found, it searches those modules in its current directory.

**A module is loaded only once in a particular program, without being affected by the number of times the module is imported.**

**Syntax:**

```python
**import** module_name
```

**Example:**

```python
**import** collections
```
