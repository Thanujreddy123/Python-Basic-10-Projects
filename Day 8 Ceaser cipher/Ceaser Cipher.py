def encrypt(text, shift):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        newposition = (position + shift) % 26
        newletter = alphabet[newposition]
        result = result + newletter
    print("This is your encrypted text:->" + result)


def decrypt(text, shift):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        newposition = (position - shift)
        if (newposition < 0):
            newposition = newposition + 26
        newletter = alphabet[newposition]
        result = result + newletter
    print("This is your decrypted text:->" + result)


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

flag = "yes"

while flag == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    flag = input("you want to continuw?yes or no:->")
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

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
