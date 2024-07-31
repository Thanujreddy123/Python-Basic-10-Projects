print("You want to play hangman you have to guess the word")
words = ["thanuj", "reddy", "bunny"]
import random
import hangman_words
import hangman_art
lifes = 6
word = random.choice(hangman_words.word_list)
print(hangman_art.logo)

print(word)

flag = True
display = []
for i in range(0, len(word)):
    display += "_"

while flag:
    guess = input("guess the letter: ")

    print(display)

    if guess in display:
        print("you guessed this already")


    for i in range(0, len(word)):
        letter = word[i]
        if letter == guess:
            display[i] = guess

    if '_' not in display:
        flag = False
    if guess not in display:
      print("you guessed a wrong word try next time")
      lifes=lifes-1;
      if lifes==0:
        flag=False
        print("you lose")
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lifes])
