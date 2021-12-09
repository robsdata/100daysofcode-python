#Write your code below this line 👇


#un numero primo es divisible entre el mismo y 1

number = 0

def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



