from math import *
import turtle as t

t.shape('circle')
t.speed(1000)
def big_circle():
    t.color('yellow')
    t.begin_fill()
    for x in range(72):
        t.forward(10)
        t.left(5)
    t.end_fill()
def eye():
    t.color('blue')
    t.begin_fill()
    for x in range(72):
        t.forward(1)
        t.left(5)
    t.end_fill()
def duga():
    t.color('red')
    t.right(90)
    for y in range(36):
        t.forward(2)
        t.right(5)
    t.forward(1)
big_circle()
t.goto(50,150)
eye()
t.penup()
t.goto(-50,150)
t.pendown()
eye()
t.penup()
t.goto(0,90)
t.pendown()
t.color('black')
t.width(10)
t.goto(0,60)
t.penup()
t.goto(15,50)
t.pendown()
duga()
