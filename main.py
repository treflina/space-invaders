from turtle import Turtle, Screen
from itertools import chain
from spaceship import Ship
from scoreboard import Scoreboard
import time
from aliens import Aliens
from bullet import Bullet
from lives import Lives
from ufo import Ufo
import random
from playsound import playsound

screen = Screen()
background_picture = Turtle()
screen.setup(width=660, height=720)
screen.bgpic("/media/heaven2.gif")
screen.title("Space Invaders")

screen.addshape(name="/media/alien20.gif")
screen.addshape(name="/media/invader.gif")
screen.addshape(name="/media/invader2.gif")
screen.addshape(name="/media/spaceship.gif")
screen.addshape(name="/media/ufo.gif")

scoreboard = Scoreboard()
lives = Lives()

aliens = Aliens()
aliens_list = aliens.aliens_row3 + aliens.aliens_row2 + aliens.aliens_row1

screen.tracer(0)
ship = Ship()
bullet = Bullet()
ufo = Ufo()

# Create barriers
shield_points = []
xcor_shield = chain(range(-240, -150, 10), range(-110, -20, 10), range(20, 110, 10), range(150, 240, 10))
for i in xcor_shield:
    for j in range(-245, -205, 10):
        shield = Turtle()
        shield.shape("square")
        shield.shapesize(0.5, 0.5)
        shield.color("chartreuse")
        shield.speed("fastest")
        shield.penup()
        shield.goto(i, j)
        shield_points.append(shield)

nextbullet_can_go = True


def gun():
    global nextbullet_can_go
    if nextbullet_can_go:
        nextbullet_can_go = False
        x = ship.xcor()
        y = ship.ycor() + 15
        bullet.setposition(x, y)
        bullet.showturtle()


# Detect collisions

def is_collided_with(a, b):
    if abs(a.xcor() - b.xcor()) < 15 and abs(a.ycor() - b.ycor()) < 15:
        return True
    else:
        return False


def is_collided_with_ship(a, b):
    if abs(a.xcor() - b.xcor()) < 28 and abs(a.ycor() - b.ycor()) < 20:
        return True
    else:
        return False


def is_collided_with_shield(a, b):
    if abs(a.xcor() - b.xcor()) < 5.5 and abs(a.ycor() - b.ycor()) < 5.5:
        return True
    else:
        return False


def is_collided_with_ufo(a, b):
    if abs(a.xcor() - b.xcor()) < 25 and abs(a.ycor() - b.ycor()) < 12:
        return True
    else:
        return False


# Create aliens' bullets

all_bullets = []


def create_alien_bullet():
    random_chance = random.randint(1, 20)
    if random_chance == 1:
        random_alien = random.choice(aliens_list)
        alien_bullet = Turtle("triangle")
        alien_bullet.shapesize(stretch_wid=0.2, stretch_len=1)
        alien_bullet.penup()
        alien_bullet.color("red")
        alien_bullet.setheading(270)
        alien_bullet.speed("fastest")
        alien_bullet.setposition(random_alien.xcor(), random_alien.ycor())
        all_bullets.append(alien_bullet)


def move_alien_bullets():
    for a_bullet in all_bullets:
        a_bullet.goto(a_bullet.xcor(), a_bullet.ycor() - 10)
        for shield_point in shield_points:
            if is_collided_with_shield(shield_point, a_bullet):
                a_bullet.hideturtle()
                all_bullets.remove(a_bullet)
                shield_point.hideturtle()
                shield_points.remove(shield_point)
                print("True")
        if is_collided_with_ship(a_bullet, ship):
            a_bullet.hideturtle()
            playsound("/media/explosion2.wav")
            lives.change_num_lives()
            lives.hideturtle()
            if lives.num_lives == 0:
                lives.game_over()
                ship.hideturtle()
            else:
                ship.setposition(0, -320)
                for a_bullet in all_bullets:
                    a_bullet.goto(a_bullet.xcor() + 1000, a_bullet.ycor() + 1000)


screen.listen()
screen.onkey(ship.move_left, "Left")
screen.onkey(ship.move_right, "Right")
screen.onkey(gun, "space")

ufos = []
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    aliens.move_left()
    create_alien_bullet()
    move_alien_bullets()

    for shield_point in shield_points:
        if is_collided_with_shield(shield_point, bullet):
            shield_point.hideturtle()
            shield_points.remove(shield_point)
            bullet.hideturtle()
            nextbullet_can_go = True

    if len(aliens.aliens_row1) > 0:
        if aliens.aliens_row1[0].xcor() < -300 or aliens.aliens_row1[-1].xcor() > 290:
            aliens.move_down()
            aliens.bounce()
    elif len(aliens.aliens_row2) > 0:
        if aliens.aliens_row2[0].xcor() < -300 or aliens.aliens_row2[-1].xcor() > 290:
            aliens.move_down()
            aliens.bounce()
    elif len(aliens.aliens_row3) > 0:
        if aliens.aliens_row3[0].xcor() < -300 or aliens.aliens_row3[-1].xcor() > 290:
            aliens.move_down()
            aliens.bounce()

    # Create ufos - random time
    if not ufos:
        r = random.randint(1, 50)
        if r == 1:
            ufo.create_ufo()
            ufos.append(ufo)
    for ufo in ufos:
        ufo.showturtle()
        ufo.move()
        if ufo.xcor() > 400:
            ufos.remove(ufo)

    # Make player's bullet disappear
    ycor_list = []
    for alien in aliens_list:
        ycor_list.append(alien.ycor())
    if len(ufos) > 0:
        if max(ycor_list) + 10 < bullet.ycor() and ufo.xcor() < -375:
            nextbullet_can_go = True
            bullet.hideturtle()
        elif max(ycor_list) + 10 < bullet.ycor() and ufo.xcor() > 340:
            nextbullet_can_go = True
            bullet.hideturtle()
    else:
        if max(ycor_list) + 10 < bullet.ycor():
            nextbullet_can_go = True
            bullet.hideturtle()
    if bullet.ycor() > 305:
        nextbullet_can_go = True
        bullet.hideturtle()

    for alien in aliens_list:
        if alien.ycor() < -260:
            scoreboard.game_over()
            ship.hideturtle()

    if not nextbullet_can_go:
        bullet.goto(bullet.xcor(), bullet.ycor() + 15)
        for alien1 in aliens.aliens_row3:
            if is_collided_with(bullet, alien1):
                playsound("/media/explosion1.wav")
                scoreboard.increase_score(10)
                nextbullet_can_go = True
                bullet.hideturtle()
                alien1.hideturtle()
                aliens.aliens_row3.remove(alien1)

        for alien2 in aliens.aliens_row2:
            if is_collided_with(bullet, alien2):
                playsound("/media/explosion1.wav")
                scoreboard.increase_score(20)
                nextbullet_can_go = True
                bullet.hideturtle()
                alien2.hideturtle()
                aliens.aliens_row2.remove(alien2)

        for alien3 in aliens.aliens_row1:
            if is_collided_with(bullet, alien3):
                playsound("/media/explosion1.wav")
                scoreboard.increase_score(30)
                nextbullet_can_go = True
                bullet.hideturtle()
                alien3.hideturtle()
                aliens.aliens_row1.remove(alien3)

        if len(aliens.aliens_row1) == 0 and len(aliens.aliens_row2) == 0 and len(aliens.aliens_row3) == 0:
            scoreboard.player_win()
            ship.hideturtle()

        if -350 < ufo.xcor() < 350 and ufo.xcor() != 0 and ufo.ycor() != 0:
            if is_collided_with_ufo(ufo, bullet) is True:
                playsound("/media/explosion1.wav")
                scoreboard.increase_score(100)
                nextbullet_can_go = True
                bullet.hideturtle()
                ufo.hideturtle()
                ufos.remove(ufo)

screen.update()
screen.exitonclick()
