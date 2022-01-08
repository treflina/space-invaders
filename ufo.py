from turtle import Turtle


class Ufo(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def create_ufo(self):
        self.shape("/media/ufo.gif")
        self.setposition(-500, 300)
        self.setheading(0)
        self.penup()
        self.speed("slowest")

    def move(self):
        self.goto(self.xcor() + 5, 300)
