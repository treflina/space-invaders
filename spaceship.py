from turtle import Turtle


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("spaceship.gif")
        self.x_move = 15
        self.setposition(0, -320)
        self.move_speed = 6

    def move_left(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, -320)

    def move_right(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, -320)
