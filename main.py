from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    time_label['text'] = 'Timer'
    check_mark_label['text'] = ''
    canvas.itemconfig(time_text, text='00:00')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text='Long Break', foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text='Short Break', foreground=PINK)
    else:
        count_down(work_sec)
        time_label.config(text='Working Time', foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #print(count)
    count_min = floor(count / 60)   # takе the whole number (4.98 => 4)
    count_sec = count % 60  # take only remainders (299 = (60 * 4) + 59 => 59)
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(time_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(50, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_session = floor(reps/2)
        for _ in range(work_session):
            marks += '✔'
            check_mark_label['text'] = marks

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text='Timer', font=(FONT_NAME, 50), foreground=GREEN, bg=YELLOW)
time_label.grid(column=1, row=0)

check_mark_label = Label(foreground=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_btn = Button(text='Start', command=start_timer, font=FONT_NAME, borderwidth=0, highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', font=FONT_NAME, borderwidth=0, highlightthickness=0)
reset_btn.grid(column=2, row=2)


window.mainloop()
