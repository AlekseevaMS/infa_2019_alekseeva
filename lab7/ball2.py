from tkinter import *
from random import randrange as rnd, choice
import time
import math

colors = ['red','orange','yellow','green','blue']

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __iadd__(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self
    
    def __add__(self, vector):
        return Vector(self.x + vector.x,self.y + vector.y)
    
    def __isub__(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        return self
    
    def __isub__(self, vector):
        return Vector(self.x - vector.x,self.y - vector.y)
    
    def __imul__(self, c):
        self.x *= c
        self.y *= c
        return self
    
    def __mul__(self, c):
        return Vector(self.x * c, self.y * c)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def abs(self):
        return (self.x**2 + self.y**2)**0,5
    
    def norm(self):
        return Vector(self.x, self.y)*(1 / abs(self))



class Ball:
    def __init__(self, canv,x = 0, y = 0, vx = 0,vy = 0, ax = 0, ay = 0, m = 1, r = 25):
        self.p = Vector(x, y)
        self.v = Vector(vx, vy)
        self.a = Vector(ax, ay)
        self.m = m
        self.r = r
        self.rf = Vector(0, 0)
        self.o = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
            
        
    def move(self, canv, dx = 0, dy = 0, dt = 1):
        self.a = self.rf
        print(self.v.x, self.v.y)
        self.v += self.a * dt
        dp = self.v * dt
        self.p += dp
        canv.move(self.o, dp.x, dp.y)

    
    def reflection(self, w, h):
        if self.p.x < self.r:
            self.a.x = self.r - self.p.x
        elif self.p.x > w - self.r:
            self.a.x = w - self.p.x - self.r
        else:
            self.a.x = 0
        if self.p.y < self.r:
            self.a.y = self.r - self.p.y
        elif self.p.y > h - self.r:
            self.a.y = h - self.p.y - self.r
        else:
            self.a.y = 0

            
    def collision(self, ball):
        d = self.dist(ball)
        if d < 0:
            r = self.r + ball.r + d
            sin = math.fabs((self.p.x - ball.p.x) / (
                    ((self.p.x - ball.p.x) ** 2 + (self.p.y - ball.p.y) ** 2) ** (1 / 2)))
            cos = math.fabs((self.p.y - ball.p.y) / (
                    ((self.p.x - ball.p.x) ** 2 + (self.p.y - ball.p.y) ** 2) ** (1 / 2)))
            if self.p.x > ball.p.x:
                self.rf.x = r * sin
                ball.rf.x = - r * sin
            else:
                self.rf.x = - r * sin
                ball.rf.x = r * sin
            if self.p.y > ball.p.y:
                self.rf.y = r * cos
                ball.rf.y = - r * cos
            else:
                self.rf.y = - r * cos
                ball.rf.y = r * cos

    def check(self, ball):
        if ((self.p.x - ball.p.x) ** 2 + (self.p.y - ball.p.y) ** 2) ** (1 / 2) < (self.r + ball.r):
            self.t +=1

    def dist(self, ball):
        return ((self.p.x - ball.p.x) ** 2 + (self.p.y - ball.p.y) ** 2) ** (1 / 2) - (self.r + ball.r)
        
    
    
    def zerorf(self):  
        if self.t == 0:
            self.rf.x = 0
            self.rf.y = 0

    def slowdown(self, k): 
        if math.fabs(self.vel.x) > 5:
            self.airres.x = -1 * k * (self.v.x) * math.fabs(self.v.x)
        if math.fabs(self.v.y) > 5:
            self.airres.y = -1 * k * (self.v.y) * math.fabs(self.v.y)            


class World:
    def __init__(self, w, h, n):
        self.w = w
        self.h = h
        self.n = n
        self.dt = 1
        self.root = Tk()
        self.root.geometry('%sx%s' % (w, h))# вызов окна
        self.canv = Canvas(self.root,bg='white')
        self.canv.pack(fill=BOTH,expand=1)
        self.create_balls()
    
    def create_balls(self):
        self.balls = []
        for i in range(self.n):
            x = rnd(100,700)
            y = rnd(100,500)
            #vx = rnd(-10,10)
            #vy = rnd(-10,10)
            vx = vy = 0
            r = rnd(30,50)
            self.balls.append(Ball(self.canv, x, y, vx, vy, r=r))
            

    def update(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                self.balls[i].collision(self.balls[j])
        for ball in self.balls:
            ball.reflection(self.w, self.h)
            print(ball.p)
            ball.move(self.canv, dt=self.dt)

        self.root.after(self.dt, self.update)




world = World(800, 600, 10)
world.update()
mainloop() #запуск обработка главных событий
