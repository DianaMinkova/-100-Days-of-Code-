from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_random = randint(-280, 280)
        y_random = randint(-280, 280)
        self.goto(x_random, y_random)
