from turtle import Turtle                                  # Creates and returns a new turtle object.


class Paddle(Turtle):                                      # Create class Paddle with inheritance Turtle.

    def __init__(self, position):                          # The self variable and other argument
        super().__init__()                                 # represents the instance of the object
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):                                       # A method of moving a turtle
        new_y = self.ycor() + 20                           # Current position of the turtle => x/ycor()
        self.goto(self.xcor(), new_y)                      # Moves the turtle from the current pos to the location x, y

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
