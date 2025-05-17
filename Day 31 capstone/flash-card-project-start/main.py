BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random as rd
import time
window=Tk()

window.title("Flash card app")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


data=pd.read_csv("data/french_words.csv")

def shuffleword():
    new_word=data.loc[rd.randint(1,102)].French
    word_label.config(text=new_word)

def flipcards():
    language_label.config(text="English")
    word_label.config(text=data.loc[rd.randint(1,102)].English)
window.after(3000,flipcards)

card_back=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="images/card_front.png")

canvas=Canvas(width=800,height=526)
canvas.create_image(400,263,image=card_front)
canvas.grid(column=0,row=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
rightButton=Button(image=right,highlightthickness=0,command=shuffleword)
wrongButton=Button(image=wrong,highlightthickness=0,command=shuffleword)

rightButton.grid(column=1,row=1)
wrongButton.grid(column=0,row=1)


language_label=Label(text="French",font=("Ariel",40,"italic"))
canvas.create_window(400,150,window=language_label)


word_label=Label(text="trouve",font=("Ariel",60,"bold"))
canvas.create_window(400,263,window=word_label)

window.mainloop()