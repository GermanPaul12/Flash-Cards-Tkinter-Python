from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import randint, choice
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT="Ariel"
# ---------------------------- Flashcard Generator ------------------------------- #
try:
    pd_data = pd.read_csv("Flash-Cards/unknown_words.csv")
except FileNotFoundError:
    pd_data = pd.read_csv("Flash-Cards/EN Top 1000 Words.csv") 
pd_dict = pd_data.to_dict(orient="records")

turned = 1

def turn_flashcard():
    global turned
    global current_card
    turned += 1
    if turned % 2 == 0:
        canvas.itemconfig(card_bg, image=back_card_img)
        canvas.itemconfig(card_title, text="German", fill="white")
        canvas.itemconfig(card_word, text=current_card["German"], fill="white")
           
    else:
        canvas.itemconfig(card_title, text="English", fill="black")
        canvas.itemconfig(card_word, text=current_card["English"], fill="black")    
        canvas.itemconfig(card_bg, image=front_card_img)
        
        
def new_flashcard():
    global current_card
    global turned
    current_card = choice(pd_dict)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    while turned % 2 == 0:
        turn_flashcard()
    
def known_flashcard():
    global pd_dict
    global pd_data
    pd_dict.remove(current_card)  
    known_words = pd.DataFrame(pd_dict) 
    known_words.to_csv("Flash-Cards/unknown_words.csv", index=False)
    new_flashcard()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash-Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
back_card_img = PhotoImage(file="Flash-Cards/images/card_back.png") 
front_card_img = PhotoImage(file="Flash-Cards/images/card_front.png")
card_bg = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="English", font=(FONT, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=1, columnspan=3)

known_image = PhotoImage(file="Flash-Cards/images/right.png")
known_button = Button(highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, image=known_image, command=known_flashcard, borderwidth = 0)
known_button.grid(column=0, row=2)

unknown_image = PhotoImage(file="Flash-Cards/images/wrong.png")
unknown_button = Button(highlightthickness=0, bg=BACKGROUND_COLOR, image=unknown_image, command=new_flashcard, borderwidth = 0)
unknown_button.grid(column=2, row=2)

turn_around_image = PhotoImage(file="Flash-Cards/images/turn_around.png")
turn_around_button = Button(highlightthickness=0, bg=BACKGROUND_COLOR, image=turn_around_image, command=turn_flashcard, borderwidth = 0)
turn_around_button.grid(column=1, row=2)
new_flashcard()

window.mainloop()