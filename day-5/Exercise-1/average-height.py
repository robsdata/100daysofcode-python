# 🚨 Don't change the code below 👇

#User enters values separated by a space
student_heights = input("Input a list of student heights ").split()

#for n (counter) from 0 to len(list)
for n in range(0, len(student_heights)):
    #converts values str to int
    student_heights[n] = int(student_heights[n])


# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_heights = 0

for x in range(0, len(student_heights)):
    sum_heights += student_heights[x]

average_height = sum_heights / len(student_heights)

print(f"The average is a total of: {average_height:.2f}")

