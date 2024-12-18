import random
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/flash_words.csv")
to_learn = data.to_dict("records")
random_card = {}
word_count = 0
score = 0

def next_card():
    global random_card, time_counter
    window.after_cancel(time_counter)
    random_card = random.choice(to_learn)
    canvas_card.itemconfig(english_img, image=card_front_img)
    canvas_card.itemconfig(lang, text="English")
    canvas_card.itemconfig(word, text=random_card["English"])
    time_counter = window.after(3000, flip_card)

def flip_card():
    canvas_card.itemconfig(lang, text="Turkish")
    canvas_card.itemconfig(word, text=random_card["Turkish"])
    canvas_card.itemconfig(english_img, image=card_back_img)

def update_word_count():
    global word_count
    word_count += 1
    scoreboard.config(text=f"Total Words: {word_count} | Score: {score}")

def update_score():
    global score, word_count
    score += 1
    word_count += 1
    scoreboard.config(text=f"Total Words: {word_count} | Score: {score}")

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

time_counter = window.after(3000, flip_card)

scoreboard = Label(text=f"Total Words: {word_count} | Score: {score}", bg=BACKGROUND_COLOR, font=("Arial", 15, "bold"))
scoreboard.grid(row=0, column=0, columnspan=2)

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
turkish_img = canvas_card.create_image(400, 263, image=card_back_img)
english_img = canvas_card.create_image(400, 263, image=card_front_img)
lang = canvas_card.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
word = canvas_card.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas_card.grid(row=1, column=0, columnspan=2)

no_button_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_button_img, highlightthickness=0, command=lambda: [next_card(), update_word_count()])
no_button.grid(row=2, column=0)
yes_button_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_button_img, highlightthickness=0, command=lambda: [next_card(), to_learn.remove(random_card), update_score()])
yes_button.grid(row=2, column=1)

next_card()

window.mainloop()