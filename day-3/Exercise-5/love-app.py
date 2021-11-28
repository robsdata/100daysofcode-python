# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

t_count = lowercase_name1.count("t") + lowercase_name2.count("t")
r_count = lowercase_name1.count("r") + lowercase_name2.count("r")
u_count = lowercase_name1.count("u") + lowercase_name2.count("u")
e_count = lowercase_name1.count("e") + lowercase_name2.count("e")

true_count = t_count + r_count + u_count + e_count

l_count = lowercase_name1.count("l") + lowercase_name2.count("l")
o_count = lowercase_name1.count("o") + lowercase_name2.count("o")
v_count = lowercase_name1.count("v") + lowercase_name2.count("v")
e_count = lowercase_name1.count("e") + lowercase_name2.count("e")

love_count = l_count + o_count + v_count + e_count


string_lovecount = str(true_count) + str(love_count)

grand_total = int(string_lovecount)

if grand_total < 10 or grand_total > 90:
    print(f"Your score is {grand_total}, you go together like coke and mentos.")
elif grand_total > 40 and grand_total < 50:
    print(f"Your score is {grand_total}, you are alright together.")
else:
    print(f"You're score is {grand_total}")