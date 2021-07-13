from turtle import Turtle, Screen

screen = Screen()


class Aliens:

    def __init__(self):
        self.aliens_row1 = []
        self.aliens_row2 = []
        self.aliens_row3 = []
        self.create_alien()

    def create_alien(self):
        screen.tracer(0)
        y_row1 = 250
        y_row2 = 210
        y_row3 = 170
        for num_x in range(8):
            x = num_x * 40
            self.alien = Turtle()
            self.alien.penup()
            self.alien.shape("alien20.gif")
            self.alien.goto(x, y_row1)
            self.alien.x_move = 4
            self.aliens_row1.append(self.alien)
        for num_x in range(8):
            x = num_x * 40
            self.alien = Turtle()
            self.alien.penup()
            self.alien.shape("invader.gif")
            self.alien.goto(x, y_row2)
            self.alien.x_move = 4
            self.aliens_row2.append(self.alien)
        for num_x in range(8):
            x = num_x * 40
            self.alien = Turtle()
            self.alien.penup()
            self.alien.shape("invader2.gif")
            self.alien.goto(x, y_row3)
            self.alien.x_move = 4
            self.aliens_row3.append(self.alien)

    def move_left(self):
        for alien_object in self.aliens_row1:
            alien_object.goto(alien_object.xcor() - self.alien.x_move, alien_object.ycor())
        for alien_object in self.aliens_row2:
            alien_object.goto(alien_object.xcor() - self.alien.x_move, alien_object.ycor())
        for alien_object in self.aliens_row3:
            alien_object.goto(alien_object.xcor() - self.alien.x_move, alien_object.ycor())

    def move_right(self):
        for alien_object in self.aliens_row1:
            alien_object.goto(alien_object.xcor() + 4, alien_object.ycor())
        for alien_object in self.aliens_row2:
            alien_object.goto(alien_object.xcor() + 4, alien_object.ycor())
        for alien_object in self.aliens_row3:
            alien_object.goto(alien_object.xcor() + 4, alien_object.ycor())

    def bounce(self):
        self.alien.x_move *= -1

    def move_down(self):
        if len(self.aliens_row1) > 0:
            for alien_object in self.aliens_row1:
                alien_object.goto(alien_object.xcor(), alien_object.ycor() - 20)
        if len(self.aliens_row2) > 0:
            for alien_object in self.aliens_row2:
                alien_object.goto(alien_object.xcor(), alien_object.ycor() - 20)
        if len(self.aliens_row3) > 0:
            for alien_object in self.aliens_row3:
                alien_object.goto(alien_object.xcor(), alien_object.ycor() - 20)
