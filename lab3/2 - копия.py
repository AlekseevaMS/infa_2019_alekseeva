
from graph import *
from math import *
import math as m
a = []
windowSize(800, 400)
canvasSize(800, 400)

penColor(0, 0, 0)
brushColor(14, 147, 37)
rectangle(0, 225, 800, 400) #grass
brushColor(153, 227, 237)
rectangle(0, 0, 800, 225)# sky
brushColor(147, 107, 14)
rectangle(100, 200, 200, 300)#house1
brushColor(235, 47, 68)
polygon([(100,200), (150,125),
         (200,200), (100,200)])
penColor("white")
brushColor(14, 147, 145)
rectangle(127, 225, 172, 260)#window 1
penColor(0,0,0)
brushColor("white")
circle(40, 70, 25)#cloud
circle(70, 70, 25)
circle(30, 90, 25)
circle(60, 90, 25)
circle(90, 90, 25)
circle(120, 90, 25)
brushColor(0, 0, 0)
rectangle(500, 175,515, 275)#tree
brushColor(15, 83, 14)
circle(250, 100, 30)
circle(290, 120, 30)
circle(270, 120, 30)
circle(250, 140, 30)
circle(270, 160, 30)
circle(290, 160, 30)
brushColor(249, 194, 194)# sun
penColor(249, 194, 194)
n = 30
for i in range(n):
    x = 20
    y = 60
    if i%2 == 0:
        a.append((x+30*m.cos(2*m.pi*i/n), y+30*m.sin(2*m.pi*i/n)))
    else:
        a.append((x+35*m.cos(2*m.pi*i/n), y+35*m.sin(2*m.pi*i/n)))
polygon(a)
    


run()
