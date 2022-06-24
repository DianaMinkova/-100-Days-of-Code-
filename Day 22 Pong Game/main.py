from ball import Ball
from turtle import Screen                # Import turtle library to draw around using the turtle methods.
from paddle import Paddle                # Import file to use class Paddle
from scoreboard import Scoreboard
import time


screen = Screen()                        # The function Screen() returns a singleton object of a TurtleScreen subclass.
screen.title('My_Pong')                  # Set the title of turtle-window.
screen.bgcolor('black')                  # Give the color to the background.
screen.setup(width=800, height=600)      # Set the size and position of the main window.
screen.tracer(0)                         # Turn turtle animation on/off and set a delay for update drawings (0).

r_paddle = Paddle((350, 0))              # Create object of a class Paddle
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()                          # Listens for screen/window inputs.
screen.onkey(r_paddle.go_up, 'Up')       # Gets evaluated when we click on the screen,
screen.onkey(r_paddle.go_down, 'Down')   # it enables the user to perform an action.
screen.onkey(l_paddle.go_up, 'w')        # onkey(fun, btn)
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)          # Slowing down between each of the update.
    screen.update()                      # It allows only a portion of the screen to update.
    ball.move()

    # Detect bounce with wall and change direction:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect bounce with paddle and change direction:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect Right paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left paddle misses:
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()                     # Go into mainloop until the mouse is clicked.
