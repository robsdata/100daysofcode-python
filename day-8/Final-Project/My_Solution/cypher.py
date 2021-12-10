alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(user_text = text, caesar_shift_amount = shift, caesar_direction = direction):
    
    encrypted_text = ""
    
    if direction == "decode":
        caesar_shift_amount *= (-1)

    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + caesar_shift_amount
        encrypted_text += alphabet[new_position]
        
    print(f"The {direction}d text is {encrypted_text}")
    



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)