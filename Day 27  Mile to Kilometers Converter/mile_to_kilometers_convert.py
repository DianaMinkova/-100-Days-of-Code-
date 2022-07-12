from tkinter import *


def convert():
    entry_miles = float(entry.get())
    result = entry_miles * 1.609
    #result_label['text'] = result
    result_label.config(text=f'{result}')


window = Tk()
window.title('Mile to Kilometers Convert')
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

''' Label '''
equal_label = Label(text='is equal to', font=('Arial', 20))
equal_label.grid(column=0,row=1)

miles_label = Label(text='Miles', font=('Arial', 20))
miles_label.grid(column=2,row=0)

km_label = Label(text='Km', font=('Ariel', 20))
km_label.grid(column=2, row=1)

result_label = Label(text='0', font=('Arial', 20))
result_label.grid(column=1, row=1)

''' Entry '''
entry = Entry(width=10, relief='sunken', font=('Arial', 20))
entry.grid(column=1, row=0, padx=10, pady=0)


''' Button '''
button = Button(text='Calculate', width=22, command=convert)
button.grid(column=1, row=3)


window.mainloop()
