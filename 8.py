from math import *
import turtle as t

t.shape('circle')
n0 = 3
l0 = 10
def pg(n, l):
    a = 2 * pi / n
    r = l / sqrt(1 - cos(a))
    t.penup()
    t.goto(r,0)
    t.pendown()
    for i in range(0, n + 1):
        t.goto(r * cos(a * i), r * sin(a * i))
for z in range(10):
    pg(n0, l0)
    n0 += 1
    l0 += 10
