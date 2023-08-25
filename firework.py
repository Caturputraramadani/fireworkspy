import turtle
import random
import math


screen = turtle.Screen()
screen.bgcolor("black")


firework_turtle = turtle.Turtle()
firework_turtle.speed(0)
firework_turtle.hideturtle()


def draw_burst(x, y, color):
    firework_turtle.penup()
    firework_turtle.goto(x, y)
    firework_turtle.pendown()
    firework_turtle.color(color)
    for _ in range(36):
        firework_turtle.forward(50)
        firework_turtle.backward(50)
        firework_turtle.left(10)


burst_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]

for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    color = random.choice(burst_colors)
    draw_burst(x, y, color)


firework_turtle.hideturtle()
turtle.done()
