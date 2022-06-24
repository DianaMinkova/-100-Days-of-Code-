from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10                      # Size the step of movement
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move     # The direction of movement
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)               # New position

    def bounce_y(self):
        self.y_move *= -1                     # Changing/opposite the direction of movement if bounce
        self.move_speed *= 0.9

    def bounce_x(self):                       # Changing/opposite the direction of movement if bounce
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)                       # Go to zero position
        self.move_speed = 0.01                # Reset speed when game over
        self.bounce_x()                       # Change direction
