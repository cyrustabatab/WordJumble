import random
import tkinter
from tkinter import messagebox


with open('words.txt','r') as f:
    word_bank = f.readlines()




def remove(label):

    label.grid_remove()
    check_button.configure(state='active')
    if label is correct_label:
        shuffled_word = get_word_and_shuffle()
        word_label.configure(text=shuffled_word)




def check():


    user_input = guess_entry.get()

    user_input = user_input.strip().lower()

    if not user_input:
        messagebox.showerror(title='Invalid',message='Please enter something')
    elif not user_input.isalpha():
        messagebox.showerror(title='Invalid',message='Please enter only letters')
    else:

        if user_input == word: 
            correct_label.grid()
            window.after(1000,remove,correct_label)
        else:
            incorrect_label.grid()
            window.after(1000,remove,incorrect_label)


        check_button.configure(state='disabled') 
        guess_entry.delete(0,tkinter.END)




























def get_word_and_shuffle():
    global word
    word = random.choice(word_bank)
    word = word.strip().lower()
    shuffled_word = list(word)
    random.shuffle(shuffled_word)

    shuffled_word = ''.join(shuffled_word)

    return shuffled_word


title_font = ('helvetica',40,'bold')
normal_font = ('helvetica',20,'normal')

window = tkinter.Tk()
window.title('Word Jumble')
window.configure(padx=20,pady=20)
#window.minsize(width=500,height=500)


title_label = tkinter.Label(text="WORD JUMBLE",font=title_font,fg='blue')
title_label.grid(row=0,column=0,columnspan=2)


word = None
shuffled_word = get_word_and_shuffle()

word_label = tkinter.Label(text=shuffled_word,font=title_font)

word_label.grid(row=1,column=0,columnspan=2,pady=20)



guess_label = tkinter.Label(text="Guess:",font=normal_font)
guess_label.grid(row=2,column=0)

guess_entry = tkinter.Entry(font=normal_font)
guess_entry.focus_set()

guess_entry.grid(row=2,column=1)


check_button = tkinter.Button(text='CHECK',font=normal_font,command=check)

check_button.grid(row=3,column=0,columnspan=2,pady=20)



correct_label = tkinter.Label(text='CORRECT',fg='green',font=normal_font)
incorrect_label = tkinter.Label(text='INCORRECT',fg='red',font=normal_font)

correct_label.grid(row=4,column=0,columnspan=2)
correct_label.grid_remove()
incorrect_label.grid(row=4,column=0,columnspan=2)
incorrect_label.grid_remove()


















window.mainloop()





