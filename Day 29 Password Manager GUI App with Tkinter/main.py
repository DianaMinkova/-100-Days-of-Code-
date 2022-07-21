from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from pyperclip import copy


# -------------------------------- PASSWORD GENERATOR ------------------------------ #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '?', '-']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    pass_list = []
    letters_list = [pass_list.append(choice(letters)) for let in range(randint(8, 18))]
    symbols_list = [pass_list.append((choice(symbols)))for symbol in range(randint(2, 4))]
    numbers_list = [pass_list.append((choice(numbers))) for num in range(randint(2, 4))]

    shuffle(pass_list)
    password = ''.join(pass_list)
    password_entry.insert(0, password)
    copy(password)


# -------------------------------- SAVE PASSWORD -------------------------------- #
def save():
    website = website_entry.get()
    email= email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                              f'\n{password} \nIs it ok to save?')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# -------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username :')
email_label.grid(column=0, row=2)

password_label = Label(text='Password :')
password_label.grid(column=0, row=3)


website_entry = Entry(width=35, borderwidth=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()


email_entry = Entry(width=35, borderwidth=1)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, 'diana@yahoo.com')

password_entry = Entry(width=21, borderwidth=1)
password_entry.grid(column=1, row=3, sticky="ew")

generate_pass_btn = Button(text='Generate Password', command=pass_generator, borderwidth=1)
generate_pass_btn.grid(column=2, row=3, padx=5, sticky="ew")

add_btn = Button(text='Add', command=save, width=36, borderwidth=1)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
