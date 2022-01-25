import turtle
from turtle import *

speed("fastest")

hideturtle()           #make the turtle invisible
penup()                #don't draw when turtle moves
goto(-30, -400)       #move the turtle to a location
showturtle()           #make the turtle visible
pendown()

rt(-90)

angle = 30


def y(sz, level):
    if level > 0:
        colormode(255)

        pencolor(0, 255 // level, 0)

        fd(sz)
        rt(angle)

        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)
        lt(2 * angle)

        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)

        fd(-sz)


y(175, 15)

turtle.Screen().exitonclick()