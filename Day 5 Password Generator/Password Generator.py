#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
sum=""
for i in range(0,nr_letters):
  position=random.randint(0,51)
  sum=sum+letters[position]
for i in range(0,nr_symbols):
  position=random.randint(0,10)
  sum=sum+numbers[position]
for i in range(0,nr_numbers):
  position=random.randint(0,9)
  sum=sum+symbols[position]
print(sum)

#if you want you can user random.choice(list) to select the random character
#if you want hard password generator store this in the list and use random.shuffle() to make password so difficult to crack
  