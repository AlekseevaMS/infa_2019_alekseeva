from math import *
import turtle as t

t.shape('circle')
t.speed(1000)
t.left(90)
k = 0
def infinity():
    for x in range(72):
        t.forward(5 + k)
        t.left(5)
    for y in range(72):
        t.forward(5 + k)
        t.right(5)
for i in range(7):
    infinity()
    k += 1
