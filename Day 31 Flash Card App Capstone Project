from tkinter import *
from pandas import DataFrame, read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

#---------------------------- Reading data -----------------------------
#data = read_csv('data/bg_words.csv')
#to_learn = data.to_dict(orient='records')
# print(to_learn) # => [{'French': 'partie', 'English': 'part'}...]
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/bg_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_word():
    # len_dict = len(to_learn)
    # random_num = randint(2, len_dict)
    # random_word_bg = to_learn[random_num]['en']
    # random_word2 = to_learn[randint(2, len(to_learn))]
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = choice(to_learn)
    canvas.itemconfigure(card_title, text='English', fill='black')
    canvas.itemconfigure(card_word, text=current_card['en'], fill='black')
    canvas.itemconfig(canvas_en_img, image=en_img)
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfigure(card_title, fill='white', text='Bulgaria')
    canvas.itemconfigure(card_word, fill='white', text=current_card['bg'])
    canvas.itemconfig(canvas_en_img, image=bg_img)


def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


window = Tk()
window.title('Flash cards')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = PhotoImage(file="images/card_back.png")
en_img = PhotoImage(file="images/card_front.png")
canvas_en_img = canvas.create_image(410, 280, image=en_img)
card_title = canvas.create_text(400, 150, text='', font=(FONT_NAME,  30, 'italic'))
card_word = canvas.create_text(400, 253, text='', font=(FONT_NAME, 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


""" Button """
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, padx=50, pady=50, highlightthickness=0, command=new_word)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, padx=50, pady=50, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

new_word()


window.mainloop()
