from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-300, 320)
        self.hideturtle()
        self.update_scoreboard()
        self.speed("fastest")

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def player_win(self):
        self.goto(0, 0)
        self.write("YOU WON!!!", align=ALIGNMENT, font=FONT)

    def increase_score(self, score):
        self.score += score
        self.clear()
        self.update_scoreboard()
