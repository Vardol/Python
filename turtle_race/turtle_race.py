from time import sleep
from turtle import *
from random import randint
import turtle

STARTPOSITION = -300
FINISHPOSITION = 300

def markdown():
    road_worker_turtle = Turtle()
    road_worker_turtle.speed(0)
    for i in range(1, 30):
        road_worker_turtle.penup()
        road_worker_turtle.goto(STARTPOSITION + i * 20, -50)
        road_worker_turtle.pendown()
        road_worker_turtle.goto(STARTPOSITION + i * 20, 50)
    road_worker_turtle.color("red")
    road_worker_turtle.penup()
    road_worker_turtle.goto(STARTPOSITION + i * 20, -50)
    road_worker_turtle.pendown()
    road_worker_turtle.goto(STARTPOSITION + i * 20, 50)
    road_worker_turtle.hideturtle()

def catch1_click(x, y):
    turtle1.write('Ouch!', font=('Arial', 14, 'normal'))
    turtle1.forward(randint(10, 15))

def catch2_click(x, y):
    turtle2.write('Ouch!', font=('Arial', 14, 'normal'))
    turtle2.forward(randint(10, 15))

markdown()

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("blue")
turtle1.penup()
turtle1.goto(STARTPOSITION, 20)
turtle1.pendown
turtle1.onclick(catch1_click)

turtle2 = Turtle()
turtle2.shape("turtle")
turtle2.color("green")
turtle2.penup()
turtle2.goto(STARTPOSITION, -20)
turtle2.pendown
turtle2.onclick(catch2_click)

while turtle1.xcor()<FINISHPOSITION and turtle2.xcor()<FINISHPOSITION:
    turtle1.forward(randint(1, 10))
    turtle2.forward(randint(1, 10))
    sleep(0.05)



input()