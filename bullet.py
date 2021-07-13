from turtle import Turtle


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("triangle")
        self.color("orange")
        self.penup()
        self.shapesize(0.2, 1)
        self.setheading(90)
        self.speed("fastest")
