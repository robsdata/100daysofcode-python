
text = "civilization"
shift = 3
encrypted_list = []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text_inlist = [letter for letter in text]


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

print(encrypted_list)
print(encrypted_text)



