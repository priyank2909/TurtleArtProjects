import turtle

turtle.Screen().bgcolor("black")

ninja = turtle.Turtle()

ninja.speed('fastest')
ninja.penup()
ninja.goto(0, -193)
ninja.pendown()
ninja.color("white")
ninja.circle(193)
ninja.penup()
ninja.goto(0,0)
ninja.pendown()

for i in range(180):
    ninja.color("orange")
    ninja.forward(70)
    ninja.right(30)
    ninja.color("white")
    ninja.forward(30)
    ninja.color("blue")
    ninja.forward(10)
    ninja.color("white")
    ninja.forward(30)
    ninja.left(60)
    ninja.color("green")
    ninja.forward(70)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()

    ninja.right(2)

    if i == 180:
        ninja.penup()
        break

turtle.Screen().exitonclick()