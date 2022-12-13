import os
import random
from tkinter import *
from tkinter import ttk
from string import ascii_uppercase
from tkinter import messagebox

spelling_list = []
chosen_word = ""
window = Tk
lblWord = Label
image_container = Canvas
canvas = Canvas
number_of_guesses = 0
imgLabel = Label

MAX_NUM_GUESSES = 6 #len(photos)
FILENAME = "spelling_list.txt"

def main():

    global spelling_list
    global window
    
    global MAX_NUM_GUESSES 
    global FILENAME  

    window = Tk()
    window.title("Spelling List Hangman - Lauren Snyder - CSE111")

    window.configure(background="white")
    window.geometry("1065x685")
    style = ttk.Style()
    style.theme_use('clam')
    window.config(padx=20, pady=20)     

    spelling_list = create_spelling_list_from_file(FILENAME)

    draw_label()
    draw_hangman_start()
    draw_keyboard()

    draw_new_game_btn()
    draw_spelling_list(spelling_list) 
    draw_action_buttons()

    window.mainloop()  


def draw_label():

    label=Label(window, text="Spelling List Hangman", bg="white", font=("Arial", 25))
    label.grid(column=0, row=0, columnspan=3, pady=20)

def draw_hangman_start():

    img = PhotoImage(file="./images/hangman_start.png") 

    imgLabel=Label(window, bg="white")
    imgLabel.grid(row=1, column=0, columnspan=3, sticky=W ) #padx=10, pady=40
    imgLabel.config(image=img)
    imgLabel.img = img

def draw_keyboard():
    keyboard_frame = Frame(window, width=400, height=200, bg="white")
    keyboard_frame.grid(column=0, row=3, columnspan=3)

    n = 0
    for alpha in ascii_uppercase:
        Button(keyboard_frame, text=alpha, command=lambda alpha=alpha: guess(alpha), bg="white", font=('Arial 18'), width=4).grid(row=1+n//13,column=n%13)
        n += 1

def draw_new_game_btn():
    
    new_game_button = Button(window, text="New Game", width=11, bg="white", font=("Arial", 18), command=lambda: new_game())
    new_game_button.grid(column=3, row=0, pady=5, sticky=S)

def draw_spelling_list(spelling_list):

    global spelling_listbox

    spelling_listbox=Listbox(window, height=17, width=14, font=('Arial 14'))
    spelling_listbox.grid(column=3, row=1, pady=35, padx=5, sticky=N)

    for item in spelling_list:
        spelling_listbox.insert(END, item)
    
def draw_action_buttons():
    spelling_listbox = draw_spelling_list(spelling_list)

    # Action Buttons
    add_word_button = Button(window, text="Add Word", width=15, command=lambda: add_word_window())
    add_word_button.grid(column=3, row=3, sticky=N)

    remove_word_button = Button(window, text="Remove Word", width=15, command=lambda: remove_word_window())
    remove_word_button.grid(column=3, row=3)

    hide_list_box_button = Button(window, text="Hide List", width=15, command="hide_list")
    hide_list_box_button.grid(column=3, row=3, sticky=S)

def create_spelling_list_from_file(filename):
    spelling_list = []

    #Add a try catch here for "FileNotFoundError"
    directory = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(directory, filename)

    # Open file to read spelling words
    spelling_file = open(filepath)
    
    # Read each word from file and add it to the list
    for word in spelling_file:
        spelling_list.append(word.strip(" \n"))

    return spelling_list

def get_random_word_from(spelling_list):
    word = random.choice(spelling_list)
    return word

def hide_list():
    pass
    # hide the list box

def new_game():
    global spelling_list
    global chosen_word
    global lblWord

    chosen_word = get_random_word_from(spelling_list)
    print(f"Chosen_word: {chosen_word}")
    
    # Hangman word label
    lblWord = ""
    lblWord = StringVar() 
    Label(window, textvariable = lblWord, bg="white", font=("Arial", 25)).grid(column=1, row=1, rowspan=2, sticky=E, padx=10)
    lblWord.set(' '.join("_"*len(chosen_word)))


def guess(letter):
    global number_of_guesses
    global chosen_word
    global lblWord
    global image_container
    global canvas
    global imgLabel

    not_found = []
    letter = letter.lower()
    chosen_word_with_spaces = " ".join(chosen_word[::1])

    photos = [PhotoImage(file="./images/hangman_01.png"), 
          PhotoImage(file="./images/hangman_02.png"), 
          PhotoImage(file="./images/hangman_03.png"),
          PhotoImage(file="./images/hangman_04.png"), 
          PhotoImage(file="images/hangman_05.png"), 
          PhotoImage(file="images/hangman_06.png")]
    
    print(f"Letter: {letter}")
    print(f"Chosen_word: {chosen_word}")
    print(f"chosen_word_with_spaces: {chosen_word_with_spaces}")

    screen_word = lblWord.get()
    print(f"screen_word: {screen_word}")  

    # number_of_guesses = 0
    print(f"NUMBER OF GUESSES: {number_of_guesses}")

    if number_of_guesses < MAX_NUM_GUESSES:	
        txt = list(chosen_word_with_spaces)
        guessed = list(lblWord.get())
        if chosen_word_with_spaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
            if lblWord.get()==chosen_word_with_spaces:
                messagebox.showinfo("Spelling List Hangman","Yay! You guessed it!")
                window.destroy()
        else:
            img = photos[number_of_guesses]

            imgLabel=Label(window, bg="white")
            imgLabel.grid(row=1, column=0, columnspan=3, sticky=W ) #padx=10, pady=40
            imgLabel.config(image=img)
            imgLabel.img = img

            number_of_guesses += 1

            if number_of_guesses == MAX_NUM_GUESSES:
                    messagebox.showwarning("Spelling List Hangman","Sorry. Game Over")
                    window.destroy() 

	
def close_window(top):
   top.destroy()

def add_word_to_list(top, new_word_entry):
    filename = FILENAME
    word = new_word_entry.get()

    try:
        with open(filename,"a") as file:
            file.write(word + "\n")

    except FileNotFoundError:
        messagebox.showinfo("Information","Something went wrong. We were unable to open your Spelling List File") 

    spelling_list = create_spelling_list_from_file(filename)
    draw_spelling_list(spelling_list)

    # Clear the textbox
    new_word_entry.delete(0, END)

    # Destroy the top window
    top.destroy()

def remove_word_from_list(top, listbox, delete_word): 
    filename = FILENAME
    
    spelling_list = create_spelling_list_from_file(filename)

    for word in list(spelling_list):
        if word in delete_word:
            spelling_list.remove(word)    

    draw_spelling_list(spelling_list)
            
    # Removes word from listbox view
    listbox.delete(ANCHOR)

    # Close top window when done.
    top.destroy()

def remove_word_window():
    delete_word_tuple = spelling_listbox.curselection()
    
    # If selection is empty, don't open "remove word" window
    if delete_word_tuple == ():
        messagebox.showwarning("Warning", "You must select a word first")
        pass
    else:
        # Delete Word string
        delete_word = spelling_listbox.get(delete_word_tuple)

        #Create a Toplevel window
        top_remove= Toplevel(window)
            
        top_remove.geometry("250x250")
        top_remove.config(padx=20, pady=20)
        top_remove.title("Remove Word")
        
        label = Label(top_remove, text=f"Remove this word? { delete_word}", font=("Arial", 11))
        label.grid(column=0, row=0, pady=10, sticky=W)

        #Create a Button to print something in the Entry widget
        add_word_button = Button(top_remove, text= "Remove", width=27, command= lambda:remove_word_from_list(top_remove, spelling_listbox, delete_word))
        add_word_button.grid(column=0, row=2, pady=10, sticky=W)

        #Create a Button Widget in the Toplevel Window
        cancel_button= Button(top_remove, text="Cancel", width=27, command=lambda:close_window(top_remove))
        cancel_button.grid(column=0, row=3, pady=10, sticky=W)

def add_word_window():
    
    #Create a Toplevel window
    top= Toplevel(window)
        
    top.geometry("250x250")
    top.config(padx=20, pady=20)
    top.title("Add a Word to Spelling List")
    
    label = Label(top, text="Add Word: ", font=("Arial", 11))
    label.grid(column=0, row=0, pady=10, sticky=W)

    #Create an Entry Widget in the Toplevel window
    new_word_entry= Entry(top, width=33)
    new_word_entry.grid(column=0, row=1, pady=10, sticky=W)

    #Create a Button to print something in the Entry widget
    add_word_button = Button(top, text= "Add Word", width=27, command= lambda:add_word_to_list(top, new_word_entry))
    add_word_button.grid(column=0, row=2, pady=10, sticky=W)

    #Create a Button Widget in the Toplevel Window
    cancel_button= Button(top, text="Cancel", width=27, command=lambda:close_window(top))
    cancel_button.grid(column=0, row=3, pady=10, sticky=W)
    

if __name__ == "__main__": 
    main()
