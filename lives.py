from turtle import Turtle

ALIGNMENT = "right"
FONT = ("Courier", 24, "normal")


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.num_lives = 3
        self.color("white")
        self.penup()
        self.goto(250, 320)
        self.hideturtle()
        self.update_livesboard()

    def update_livesboard(self):
        self.write(f"Lives: {self.num_lives}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def change_num_lives(self):
        if self.num_lives > 0:
            self.num_lives -= 1
            self.clear()
            self.update_livesboard()
