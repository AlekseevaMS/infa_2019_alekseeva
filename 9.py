from math import *
import turtle as t

t.shape('circle')
t.speed(1000)
def infinity():
    for x in range(72):
        t.forward(5)
        t.left(5)
    for y in range(72):
        t.forward(5)
        t.right(5)
for i in range(3):
    infinity()
    t.left(60)
