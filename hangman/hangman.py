from time import sleep
from tkinter import *
import random
from hangman_parts import parts

root = Tk()

# Creating a label widget
myLabel = Label(root, text="Hello World!")

# Shoving it onto the screen
myLabel.pack()

root.mainloop()

#Prints a hangman picture
print("Welcome to Hangman")
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|    O')
print('   ',  '|   -|-')
print('   ',  '|    |')
print('   ',  '|   / \\')
print('------------')

print(f"Picking a spelling word from your spelling list")

spelling_words = ["hello", "garage", "christmas"]
chosen_word = random.choice(spelling_words)

print(f"Your spelling word has {len(chosen_word)} letters.")

found = ['_'] * len(chosen_word)
not_found = []

def update():
    for i in found: 
        print(i, end=' ')
    print()

def wait():
    for i in range(5):
        print('.', end= '')
        sleep(.5)
    print()

wait()
update()

while True: 

    guess = input(f"Guess a letter for the spelling word: ")

    if guess in chosen_word: 
        index = 0
        for i in chosen_word:
            if i == guess:
                found[index] = guess
            index += 1
        update()
    else:
        if guess not in not_found:
            not_found.append(guess)
        else: 
            print(f"You already guessed that.")            
        print(not_found)

    # The max amount of wrong tries:
    if len(not_found) >= 5: 
        print("Sorry! You lose.")
        print(f"Your spelling word was: {chosen_word}")
        break

    if '_' not in found: 
        print(f"You win!")
        break
