from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import randint, choice
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT="Ariel"
# ---------------------------- Flashcard Generator ------------------------------- #
try:
    pd_data = pd.read_csv("/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Flash-Cards/unbekannte_wörter.csv")
except FileNotFoundError:
    pd_data = pd.read_csv("/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Flash-Cards/DE Top 1000 Words.csv") 
pd_dict = pd_data.to_dict(orient="records")

turned = 1
language_code = 0
def change_language_us():
    global language_code
    canvas.itemconfig(card_bg, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    language_code = 0
def change_language_ru():
    global language_code
    canvas.itemconfig(card_bg, image=back_card_img)
    canvas.itemconfig(card_title, text="Hа русском", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russisch"], fill="white")
    language_code = 1
def turn_flashcard():
    global turned
    global current_card
    global language_code
    turned += 1
    if turned % 2 == 0:
        if language_code == 0:
            change_language_us()
        else:
            change_language_ru()  
    else:
        canvas.itemconfig(card_title, text="Deutsch", fill="black")
        canvas.itemconfig(card_word, text=current_card["Deutsch"], fill="black")    
        canvas.itemconfig(card_bg, image=front_card_img)
        
        
def new_flashcard():
    global current_card
    global turned
    current_card = choice(pd_dict)
    canvas.itemconfig(card_title, text="Deutsch")
    canvas.itemconfig(card_word, text=current_card["Deutsch"])
    while turned % 2 == 0:
        turn_flashcard()
    
def known_flashcard():
    global pd_dict
    global pd_data
    pd_dict.remove(current_card)  
    known_words = pd.DataFrame(pd_dict) 
    known_words.to_csv("/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Flash-Cards/unbekannte_wörter.csv", index=False)
    new_flashcard()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash-Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
back_card_img = PhotoImage(file="Flash-Cards/images/card_back.png") 
front_card_img = PhotoImage(file="Flash-Cards/images/card_front.png")
card_bg = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="Deutsch", font=(FONT, 40, "italic"), fill="black")
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

ru_img = PhotoImage(file="Flash-Cards/images/ru.png")
ru_button = Button(highlightthickness=0, bg=BACKGROUND_COLOR, image=ru_img, borderwidth = 0, command=change_language_ru)
ru_button.grid(column=0, row=0)

us_img = PhotoImage(file="Flash-Cards/images/usa.png")
us_button = Button(highlightthickness=0, bg=BACKGROUND_COLOR, image=us_img, borderwidth = 0, command=change_language_us)
us_button.grid(column=2, row=0)

new_flashcard()

window.mainloop()