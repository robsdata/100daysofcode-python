"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

1 year = 365 days
1 year = 52 weeks
1 year = 12 months


Example output: 

You have 12410 days, 1768 weeks, and 408 months left.


"""

# 🚨 Don't change the code below 👇

age = input("What is your current age?")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

total_years = 90

total_years_left = total_years - age_int

total_months_left = total_years_left * 12

total_weeks_left = total_years_left * 52

total_days_left = total_years_left * 365


print(f"You have {total_days_left} days, {total_weeks_left} weeks, and {total_months_left} months left.")
