# 🐢 Import turtle module
import turtle

# 🧙‍♂️ Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# ✍️ Create turtle object
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(2)

# 🔺 Draw triangle
pen.color("purple")
for _ in range(3):
    pen.forward(100)
    pen.left(120)

pen.penup()
pen.goto(-150, 0)
pen.pendown()

# 🟦 Draw rectangle
pen.color("green")
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)

# 👋 Exit on click
screen.exitonclick()
