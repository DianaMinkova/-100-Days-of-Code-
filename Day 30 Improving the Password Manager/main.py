from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from pyperclip import copy
import json


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
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------------- PASSWORD FIND ------------------------------ #
def pass_find():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f'No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f'{website}', message=f'email: {email}\npassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')


# -------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

""" Label """
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username :')
email_label.grid(column=0, row=2)

password_label = Label(text='Password :')
password_label.grid(column=0, row=3)

""" Entry """
website_entry = Entry(width=21, borderwidth=1)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35, borderwidth=1)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, 'diana@yahoo.com')

password_entry = Entry(width=21, borderwidth=1)
password_entry.grid(column=1, row=3, sticky="ew")

""" Btn """
search_website_btn = Button(text='Search', command=pass_find, borderwidth=1)
search_website_btn.grid(column=2, row=1, padx=5, sticky="ew")

generate_pass_btn = Button(text='Generate Password', command=pass_generator, borderwidth=1)
generate_pass_btn.grid(column=2, row=3, padx=5, sticky="ew")

add_btn = Button(text='Add', command=save, width=36, borderwidth=1)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
