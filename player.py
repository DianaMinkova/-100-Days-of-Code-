from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def do_up(self):
        # current_position = self.pos()
        # new_y = current_position[1] + MOVE_DISTANCE
        # self.goto(STARTING_POSITION[0], new_y)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
