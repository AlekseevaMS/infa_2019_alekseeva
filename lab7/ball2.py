from tkinter import *
from random import randrange as rnd, choice
import time
import math

colors = ['red','orange','yellow','green','blue']

def rgb(color):
	return "#%02x%02x%02x" % color

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
	
	def __sub__(self, vector):
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
		return (self.x**2 + self.y**2)**0.5
	
	def norm(self):
		return Vector(self.x, self.y)*(1 / self.abs())



class Ball:
	def __init__(self, canv,x = 0, y = 0, vx = 0,vy = 0, ax = 0, ay = 0, r = 25):
		self.p = Vector(x, y)
		self.v = Vector(vx, vy)
		self.a = Vector(ax, ay)
		self.m = r * r
		self.r = r
		self.o = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
		self.canv = canv
			
		
	def move(self, canv, dx = 0, dy = 0, dt = 1):
		self.v += self.a * dt
		self.a = Vector(0, 0)
		dp = self.v * dt
		self.p += dp
		self.set_color()
		canv.move(self.o, dp.x, dp.y)
		p = self.p
		r = self.r
		canv.coords(self.o, p.x - r, p.y - r, p.x + r, p.y + r)
		#print(self.p - Vector(pp[0] - pp[2], pp[3] - pp[1])) 

	
	def reflection(self, w, h):
		if self.p.x < self.r:
			self.a.x += self.r - self.p.x
		elif self.p.x > w - self.r:
			self.a.x += w - self.p.x - self.r
		if self.p.y < self.r:
			self.a.y += self.r - self.p.y
		elif self.p.y > h - self.r:
			self.a.y += h - self.p.y - self.r

			
	def collision(self, ball):
		d = self.dist(ball)
		if d < 0:
			r = self.r + ball.r + d
			n = (self.p - ball.p).norm()
			self.a += n * r * 0.01 * ball.m
			ball.a -= n * r * 0.01 * self.m

	def dist(self, ball):
		return ((self.p.x - ball.p.x) ** 2 + (self.p.y - ball.p.y) ** 2) ** (1 / 2) - (self.r + ball.r)
		

	def slowdown(self, k): 
		if math.fabs(self.vel.x) > 5:
			self.airres.x = -1 * k * (self.v.x) * math.fabs(self.v.x)
		if math.fabs(self.v.y) > 5:
			self.airres.y = -1 * k * (self.v.y) * math.fabs(self.v.y)			

	def set_color(self, color = None):
		if color != None:
			self.canv.itemconfig(self.o, fill=rgb(color))
		else:
			r = int(self.v.abs())
			if r > 255:
				r = 255
			self.set_color((r, 0, 255 - r))


class World:
	def __init__(self, w, h, n, g):
		self.g = g
		self.w = w
		self.h = h
		self.dt = 0.1
		self.root = Tk()
		self.root.geometry('%sx%s' % (w, h))# вызов окна
		self.canv = Canvas(self.root,bg='white')
		self.canv.pack(fill=BOTH,expand=1)
		self.create_balls(n)
	
	def create_balls(self, n):
		self.balls = []
		self.balls.append(Ball(self.canv, 30, 30, 3, 3, r=50))	
		for i in range(n):
			x = rnd(100,700)
			y = rnd(100,500)
			vx = vy = 0
			#vx = rnd(-10,10)
			#vy = rnd(-10,10)
			r = rnd(5, 15)
			self.balls.append(Ball(self.canv, x, y, vx, vy, r=r))

	def update(self):
		for i in range(len(self.balls)):
			for j in range(i + 1, len(self.balls)):
				self.balls[i].collision(self.balls[j])
		for ball in self.balls:
			ball.a += self.g
			ball.reflection(self.w, self.h)
			ball.move(self.canv, dt=self.dt)

		self.root.after(1, self.update)




world = World(800, 600, 200, Vector(0, 0.01))
world.update()
mainloop() #запуск обработка главных событий
