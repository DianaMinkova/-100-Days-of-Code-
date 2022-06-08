from turtle import Turtle
ALIGN = 'center'
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write('Game Over', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
