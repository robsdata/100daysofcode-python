alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):
    
    text_inlist = [letter for letter in text]

    encrypted_list = []

    for letter_intext in text:
        try:
            #index - test
            #print(alphabet.index(letter_intext))
            position = shift + alphabet.index(letter_intext)
            encrypted_list.append(alphabet[position])

        except ValueError:
            # ValueError test
            # print("ValueError")
            encrypted_list.append(letter_intext)

        except IndexError:
            position = -1
            encrypted_list.append(alphabet[position])


    encrypted_text = "".join(encrypted_list)
    print(f"The encoded text is: {encrypted_text}")




#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


encrypt(text, shift)