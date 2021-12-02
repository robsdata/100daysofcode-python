## Feedback

---

Functionally, yes, they seem to be equivalent. I didn't notice anything that would make a different result. 
But if we're talking about **computation and space complexity, only creating one list would be better**. And while this is for a beginner,  one pattern I might start getting in the habit of is this:
Whenever you see yourself doing something like

```python
password = ""
for char in password_list:
    password += char
```

Instead I would use something like this:

```python
password = "".join(password_list)
```

Behind the scenes, IIRC, joining something like this is faster than what would be needed to establish a variable and then add to it in a for loop.

There are good patterns about the second one as well though. For one, **it is using indexing to get things, which is useful to fully understand when you get into algorithms**. Also, it starts its ranges at 0, which is more traditionally what you would see. In most cases, when programming, we will start at index 0 rather than index 1. **The variables in the for loops are a bit misleading though, since when you do `for x in range(number_of_letters)`, that x is always going to be a number.**