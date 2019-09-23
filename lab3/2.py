
from graph import *
from math import *
import math as m
a = []
windowSize(800, 400)
canvasSize(800, 400)

penColor(0, 0, 0)
brushColor(14, 147, 37)
rectangle(0, 225, 800, 400)
brushColor(153, 227, 237)
rectangle(0, 0, 800, 225)
brushColor(147, 107, 14)
rectangle(100, 200, 200, 300)
brushColor(235, 47, 68)
polygon([(100,200), (150,125),
         (200,200), (100,200)])
penColor("white")
brushColor(14, 147, 145)
rectangle(127, 225, 172, 260)
penColor(0,0,0)
brushColor("white")
circle(300, 50, 25)
circle(330, 50, 25)
circle(270, 80, 25)
circle(300, 80, 25)
circle(330, 80, 25)
circle(360, 80, 25)
brushColor(0, 0, 0)
rectangle(500, 175,515, 275)
brushColor(15, 83, 14)
circle(510, 100, 30)
circle(535, 120, 30)
circle(480, 120, 30)
circle(510, 140, 30)
circle(535, 160, 30)
circle(480, 160, 30)
brushColor(249, 194, 194)
penColor(249, 194, 194)
n = 30
for i in range(n):
    x = 655
    y = 60
    if i%2 == 0:
        a.append((x+30*m.cos(2*m.pi*i/n), y+30*m.sin(2*m.pi*i/n)))
    else:
        a.append((x+35*m.cos(2*m.pi*i/n), y+35*m.sin(2*m.pi*i/n)))
polygon(a)
    


run()
