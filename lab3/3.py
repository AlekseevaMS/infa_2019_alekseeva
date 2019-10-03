
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
polygon([(100,200), (150,150),
         (200,200), (100,200)])
penColor("white")#window1
brushColor(14, 147, 145)
rectangle(127, 225, 172, 260)
penColor(0,0,0)#cloud
brushColor("white")
circle(60+90, 70, 25)
circle(90+90, 70, 25)
circle(45+80, 90, 25)
circle(75+80, 90, 25)
circle(105+80, 90, 25)
circle(135+80, 90, 25)
brushColor(0, 0, 0)#tree
penColor(0, 0,0)
rectangle(280, 175,295, 275)
brushColor(15, 83, 14)
penColor(0, 0, 0)
circle(290, 110, 30)
circle(262, 130, 30)
circle(308, 130, 30)
circle(290, 150, 30)
circle(262, 170, 30)
circle(308, 170, 30)
brushColor(249, 194, 194)# sun
penColor(249, 194, 194)
n = 30
for i in range(n):
    x = 65
    y = 60
    if i%2 == 0:
        a.append((x+30*m.cos(2*m.pi*i/n), y+30*m.sin(2*m.pi*i/n)))
    else:
        a.append((x+35*m.cos(2*m.pi*i/n), y+35*m.sin(2*m.pi*i/n)))
polygon(a)
penColor(0,0,0)
brushColor("white")
circle(60+90+250, 70+20, 20)#cloud2
circle(90+90+250, 70+20, 20)
circle(45+80+250, 90+20, 20)
circle(75+80+250, 90+20, 20)
circle(105+80+250, 90+20, 20)
circle(135+80+250, 90+20, 20)
brushColor(147, 107, 14)#house2
rectangle(385, 180, 455, 250)
brushColor(235, 47, 68)
polygon([(385,180), (420,145),
         (455,180), (385,180)])
penColor("white")#window2
brushColor(14, 147, 145)
rectangle(405, 200, 435,230)

brushColor(0, 0, 0)#tree2
penColor(0, 0,0)
rectangle(470+47, 175,470+53, 245)
brushColor(15, 83, 14)
circle(470+50, 105+15, 20)
circle(455+50, 120+15, 20)
circle(485+50, 120+15, 20)
circle(470+50, 135+15, 20)
circle(455+50, 160+15, 20)
circle(485+50, 160+15, 20)
penColor(0,0,0)#cloud3
brushColor("white")
circle(470+70+90, 70+15, 25)
circle(470+70+30+90, 70+15, 25)
circle(470+40+90, 90+15, 25)
circle(470+70+90, 90+15, 25)
circle(470+70+30+90, 90+15, 25)
circle(470+70+60+90, 90+15, 25)

run()
