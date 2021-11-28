"""
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight: < 18.5
Over 18.5 but below 25 they have a normal weight: > 18.5 && < 25 
Over 25 but below 30 they are slightly overweight: > 25 && < 30 
Over 30 but below 35 they are obese: > 30 && < 35
Above 35 they are clinically obese. > 35

"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2, 2)

if bmi < 18.5:
    print(f"Your IBM is: {bmi:.1f} m/kg2. You have underweight")
elif bmi < 25:
    print(f"Your IBM is: {bmi:.1f} m/kg2. You have normal weight")
elif bmi < 30:
    print(f"Your IBM is: {bmi:.1f} m/kg2. You have slightly overweight")
elif bmi < 35:
    print(f"Your IBM is: {bmi:.1f} m/kg2. You are obese")
else:
    print(f"Your IBM is: {bmi:.1f} m/kg2. You are clinicaly obese")




