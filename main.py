from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("data/Lithuanian_words.csv")
    to_learn = data.to_dict(orient="records")

flip_timer = None

def next_card():
    global current_card, flip_timer

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    flip_timer = window.after(5000, func=flip_card)
    current_card = random.choice(to_learn)
    canvas.itemconfig(current_img, image=card_front_img)
    canvas.itemconfig(card_title, text="Lithuanian", fill= BACKGROUND_COLOR)
    canvas.itemconfig(card_word, text=current_card["Lithuanian"], fill=BACKGROUND_COLOR)

def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_img, image=card_back_img)

def is_known():
    global flip_timer, current_card, to_learn
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Gintaras")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
current_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

#Buttons
cross_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
tick_image = PhotoImage(file="../flash-card-project-start/images/right.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)
tick_button = Button(image=tick_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

next_card()

# TODO-11: Test the full cycle: mark a few words as "known", close the
#  program, and reopen it — do the words you marked as known correctly
#  stay OUT of the rotation, while everything else still appears?




window.mainloop()