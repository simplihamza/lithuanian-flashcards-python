from tkinter import *
import pandas

# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Gintaras")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg="white")
card_front_img = PhotoImage(file="../flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=1, column=1)

# # Labels
# website_label = Label(text="Website: ", font=(FONT_NAME, 8), bg="white")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username: ", font=(FONT_NAME, 8), bg="white")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password: ", font=(FONT_NAME, 8), bg="white")
# password_label.grid(row=3, column=0)
#
# # Entries
#
# website_entry = Entry(width=35, bg="white")
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=35, bg="white")
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "your.email@example.com")
# password_entry = Entry(width=18, bg="white")
# password_entry.grid(row=3, column=1, columnspan=1)
#
#Buttons
cross_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
tick_image = PhotoImage(file="../flash-card-project-start/images/right.png")
cross_button = Button(image=cross_image, highlightthickness=0)
cross_button.grid(row=2, column=0, padx=50)
tick_button = Button(image=tick_image, highlightthickness=0)
tick_button.grid(row=2, column=1, padx=50)




window.mainloop()



# TODO-1: Import 'pandas' and 'random' at the top of the file (you'll need
#  both for reading the CSV data and picking a random word).

# TODO-2: Clean up leftover commented-out code from your previous project
#  (the password manager labels/entries) — they're unrelated to this project.

# TODO-3: Set up two dictionaries/lists before your UI code:
#  - 'current_card' (starts empty, will hold whichever word is currently displayed)
#  - 'to_learn' (starts empty, will hold ALL the words still left to learn)

# TODO-4: Use a try/except to load your data:
#  - Try reading a CSV called "words_to_learn.csv" (this represents words
#    the user hasn't learned yet, from a previous session).
#  - If that file doesn't exist yet (first time running the program), fall
#    back to reading the original full word list, e.g. "french_words.csv".
#  - Either way, convert whichever DataFrame you loaded into a list of
#    dictionaries (look into a DataFrame method that converts rows into
#    a list of dicts, similar to how you built lookup structures in your
#    NATO alphabet and USA States projects) and store it in 'to_learn'.

# TODO-5: Create a 'next_card' function that:
#  - Cancels any currently scheduled "flip" timer (you'll set this up in
#    TODO-9 — think about why a leftover timer from the PREVIOUS card could
#    cause bugs if not cancelled when a new card appears).
#  - Picks a new random word from 'to_learn' and stores it in 'current_card'.
#  - Updates the canvas text and image to show the FRONT of the card
#    (the foreign-language word), using the front-side styling/colors.
#  - Schedules a new timer that will call a "flip" function after a few
#    seconds, to auto-reveal the translation.

# TODO-6: Create a 'flip_card' function that:
#  - Updates the canvas text and image to show the BACK of the card
#    (the English translation), using the back-side styling/colors.

# TODO-7: Create an 'is_known' function that:
#  - Removes the current card from 'to_learn' (since the user has confirmed
#    they know it).
#  - Saves the updated (now shorter) 'to_learn' list back out to
#    "words_to_learn.csv" using pandas, so progress persists between sessions.
#  - Calls 'next_card()' to immediately move on to a new word.

# TODO-8: Wire up your two buttons:
#  - The "wrong"/cross button should call 'next_card' directly (skip this
#    word, don't remove it from the list, just show a new one).
#  - The "right"/tick button should call 'is_known' (mark this word as
#    learned, remove it, then move to a new one).

# TODO-9: Set up the canvas so its background image, title text, and word
#  text are each stored in variables (using 'canvas.create_image()' and
#  'canvas.create_text()') so they can be updated later via 'canvas.itemconfig()'
#  — similar to how you've handled canvas updates in your Pomodoro Timer project.

# TODO-10: At the very end of your setup code, call 'next_card()' once, so
#  the very first card is displayed as soon as the program starts.