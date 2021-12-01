# 🚨 Don't change the code below 👇

#User enters values separated by a space
student_heights = input("Input a list of student heights ").split()

#for n (counter) from 0 to len(list)
for n in range(0, len(student_heights)):
    #converts values str to int
    student_heights[n] = int(student_heights[n])


# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
total_participants = 0

for height in student_heights:
    total_height += height
    total_participants += 1


average = total_height / total_participants

print(f"The average is {average:.0f}")
