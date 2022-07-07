from turtle import Screen, Turtle, shape, mainloop
from pandas import DataFrame, read_csv
screen = Screen()
screen.title('U.S. States Game') # Title name of the game

t = Turtle()
t.penup()
t.hideturtle()

image = 'blank_states_img.gif' # Only image.gif file format
screen.addshape(image) # This function is used to Add a shape to TurtleScreen.

shape(image)   # Set the shape

data = read_csv('50_states.csv')
# print(data)
state_list = data.state.to_list()  # Get all state in a list
# print(state_list)
guessed_state = [] # Add the correct answer in a new list

while len(guessed_state) <= 50:  # It is value in state
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 State Counter', prompt='What\'s another state is name?').title()
    if answer_state == 'Exit':
        # Check which states are unknown
        li_dif = [i for i in state_list + guessed_state if i not in state_list or i not in guessed_state]
        df = DataFrame(li_dif)
        print(df)
        df.to_csv('Learn_more.csv')
        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        coordinate = data[data.state == answer_state]
        # x = coordinate['x'].values[0]
        # y = coordinate['y'].values[0]
        # print(x, y)
        # t.goto(x, y)
        t.goto(int(coordinate.x), int(coordinate.y))
        t.write(answer_state)
