from colors_data import color_list
from random import choice
from turtle import Turtle, Screen, colormode


colormode(255)               # Because used rgb system
dodo = Turtle()
dodo.speed("fastest")
#dodo.penup()
dodo.hideturtle()           # This method make turtle invisible
dodo.setheading(225)        # Settings of moving directions in degree
dodo.forward(300)
dodo.setheading(0)
num_of_dots = 101


for dot_count in range(1, num_of_dots):
    dodo.dot(20, choice(color_list))
    dodo.forward(50)

    if dot_count % 10 == 0:
        dodo.setheading(90)
        dodo.forward(50)
        dodo.setheading(180)
        dodo.forward(500)
        dodo.setheading(0)


screen = Screen()           # Used to create a canvas for drawing
screen.exitonclick()
