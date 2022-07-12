from tkinter import *

''' Creating new window and configuration '''
window = Tk()  # Create new window
window.title('Widget Examples')  # Set title name
window.minsize(width=500, height=600)  # Set size in new window

''' Label '''
label = Label(text='This is old text', font=('Arial', 24, 'italic'), foreground='red', background='yellow')
#label.config(text='This is new text', font=('Times New Roman', 24, 'italic'), foreground='yellow', background='red')
label.pack()

''' Buttons '''
def action():
    print('Do something')
    label.config(text='This is new text', font=('Times New Roman', 24, 'italic'), foreground='yellow', background='red')


# Call action when pressed:
button = Button(text='Click Me', command=action, cursor="heart", width=10, height=5, background='blue',
                foreground='white', font='bold')
button.pack()

''' Entry '''
entry = Entry(width=30, background='green', foreground='white')
# Add some text to begin with
entry.insert(END, string='Please, enter your e-mail')
# Get text in entry
print(entry.get())
entry.pack()

''' Text '''
text = Text(height=5,width=30, background='red', foreground='white')
# Puts cursor in textbox
text.focus()
# Add some text to begin with
text.insert(END, 'Example of multi-line text entry')

# Get\'s current value in textbox at line 1, character 0
print(text.get('1.0', END))
text.pack()

''' Spinbox '''
def spinbox_used():
    # Get the current value in spinbox
    print(spinbox.get)


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

''' Scale '''
#Called with current scal value:
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

''' Checkbutton '''
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?', foreground='red', font='bold', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


''' Radiobutton '''
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.

radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

''' Listbox '''
def listbox_used(event):
    # Get current section from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits_list = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits_list:
    listbox.insert(fruits_list.index(item), item)

listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

window.mainloop()  # to make visible
