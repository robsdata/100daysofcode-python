# 🚨 Don't change the code below 👇

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number.



if len(position) == 2:
    v_position = int(position[1]) - 1
    h_position = int(position[0]) - 1

    if (h_position <= 3) and (v_position <= 3):
        map[v_position][h_position] = "x"

    else: 
        print("Invalid location")

else:
    print("Invalid location")


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")