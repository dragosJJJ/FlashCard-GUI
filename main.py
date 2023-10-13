from tkinter import *
import pandas, csv, random

BACKGROUND_COLOR = "#B1DDC6"
seed = {}
data = {}
try:
    data = pandas.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data = original_data.to_dict(orient= "records")
else:
    data = data.to_dict(orient="records")

#----- FLIP CARD -----#
def flip_card():
    canvas.itemconfig(bg_img, image= back_img)
    canvas.itemconfig(title, fill= "white", text="English")
    canvas.itemconfig(word, fill= "white", text=seed["English"])


#----- GENERATE RANDOM WORDS -----#

def next_card():
    global seed, flip_timer
    window.after_cancel(flip_timer)
    seed = random.choice(data)
    canvas.itemconfig(word, text= seed["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(bg_img, image= front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    data.remove(seed)
    words_to_learn = pandas.DataFrame(data)
    words_to_learn.to_csv("data/words_to_learn.csv")
    next_card()

#----- UI SETUP -----#
window = Tk()
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

front_img = PhotoImage(file=".\images\card_front.png")
back_img = PhotoImage(file=".\images\card_back.png")
right_img = PhotoImage(file=r".\images\right.png")
wrong_img = PhotoImage(file=r".\images\wrong.png")


canvas = Canvas(width=800, height= 526, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR)
bg_img = canvas.create_image(400, 263, image= front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_img, highlightthickness=0, command= is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()
