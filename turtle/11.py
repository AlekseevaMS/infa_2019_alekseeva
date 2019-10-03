from math import *
import turtle as t

t.shape('circle')
t.speed(1000)
t.left(90)

def big_duga():
    for x in range(36):
        t.forward(5)
        t.right(5)
    t.forward(5)
def small_duga():
    for y in range(36):
        t.forward(1)
        t.right(5)
    t.forward(1)
for i in range(10):
    big_duga()
    small_duga()
