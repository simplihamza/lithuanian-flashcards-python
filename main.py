from tkinter import *
import pandas
import random

data = pandas.read_csv("data/Lithuanian_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Lithuanian")
    canvas.itemconfig(card_word, text=current_card["Lithuanian"])

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Gintaras")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="../flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

#Buttons
cross_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
tick_image = PhotoImage(file="../flash-card-project-start/images/right.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)
tick_button = Button(image=tick_image, highlightthickness=0, command=next_card)
tick_button.grid(row=1, column=1)

next_card()






window.mainloop()

# TODO-1: Create your two PhotoImage objects (card_front_img and card_back_img)
#  in the global/setup area of your script, NOT inside any function. Since
#  you already have card_front_img set up this way, just add a second one
#  for the back image, using the same pattern.

# TODO-2: Create a global variable (e.g. 'flip_timer') to hold a reference
#  to whatever 'window.after()' call is currently scheduled, so it can be
#  cancelled later. It can start as None, or however you'd like to
#  initialize it before anything is scheduled.

# TODO-3: Create a 'flip_card' function that:
#  - Updates the card's title text to say "English" instead of "Lithuanian"
#    (use 'canvas.itemconfig()' on your existing 'card_title' reference).
#  - Updates the card's word text to show the CURRENT card's English
#    translation (use 'canvas.itemconfig()' on your existing 'card_word'
#    reference, and 'current_card["English"]' as the value).
#  - Changes the text color to white for both pieces of text (use the
#    'fill' parameter within 'itemconfig()').
#  - Changes the canvas background image to 'card_back_img' (use
#    'canvas.itemconfig()' on your canvas image reference, changing its
#    'image' parameter).

# TODO-4: You'll need a reference to your canvas background image, similar
#  to how 'card_title' and 'card_word' store references to their text
#  items. Right now, 'canvas.create_image(...)' isn't being stored in any
#  variable — fix this so you can later change which image it displays.

# TODO-5: 'current_card' needs to be accessible both inside 'next_card()'
#  (where it gets set) and inside 'flip_card()' (where it gets read).
#  Since it's currently a local variable inside 'next_card()', think about
#  how to make it accessible to 'flip_card()' too — consider declaring it
#  as a global variable, similar to how you've handled shared state in
#  earlier projects (like your snake game's score, or your Pomodoro timer's
#  'reps').

# TODO-6: Inside 'next_card()':
#  - Cancel any previously scheduled flip timer (using 'window.after_cancel()'
#    on your 'flip_timer' variable) BEFORE scheduling a new one — think
#    about why skipping this could cause a delayed 'flip_card()' call
#    from an OLD card to incorrectly fire on top of a NEW card the user
#    already moved to.
#  - After displaying the new card's front side (which you've already
#    done), schedule a new call to 'flip_card' after 3000 milliseconds
#    using 'window.after()', storing the returned value back into your
#    'flip_timer' variable so it can be cancelled next time.

# TODO-7: Test this phase thoroughly before moving on: does the card
#  correctly flip to show the English translation after 3 seconds? If you
#  click "next card" quickly, multiple times in a row, does only ONE flip
#  ever happen per card (not multiple overlapping ones)?