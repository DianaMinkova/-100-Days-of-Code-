from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0             # Counting score
        self.r_score = 0
        self.update_scoreboard()     # Updating result

    def update_scoreboard(self):
        self.clear()                 # Clear result on display
        self.goto(-100, 200)         # Position and font a left score
        self.write(self.l_score, align='center', font=('Courier', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 70, 'normal'))

    def l_point(self):
        self.l_score += 1           # Increase score when paddle missed
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
