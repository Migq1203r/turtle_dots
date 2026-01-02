###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
from turtle import Turtle, Screen
import random

rgb_colors = [
    (245, 243, 238),
    (246, 242, 244),
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

timmy = Turtle()
turtle.colormode(255)
timmy.pensize(15)
turtle.speed(0)
timmy.teleport(-200, 0)

x = timmy.xcor()
continue_s = True


def teleport():
    global x, continue_s
    y = timmy.ycor()
    if y != 360:
        timmy.teleport(x, y + 40)
    else:
        continue_s = False


def move():
    global continue_s
    for _ in range(10):
        timmy.color(random.choice(rgb_colors))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(40)
        timmy.pendown()
        timmy.dot(20)
    teleport()


while continue_s:
    move()
screen = Screen()
screen.exitonclick()
