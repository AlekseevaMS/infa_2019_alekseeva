from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')# вызов окна
points = 0


canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
def new_ball():

    ball =dict()
    #canv.delete(ALL)
    ball['x'] = x = rnd(100,700)
    ball['y'] = y = rnd(100,500)
    ball['r'] = r = rnd(30,50)
    ball['dx'] = rnd(-5, 6)
    ball['dy'] = rnd(-5, 6)
    ball['o'] = o = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    return ball
def move_ball(ball):
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    canv.move(ball['o'], ball['dx'], ball['dy'])
    check(ball)
def update():
    for ball in balls:
            move_ball(ball)
    root.after(10, update)

    
def check(ball):
    x = ball['x']
    y = ball['y']
    r = ball['r']
    if x>800 - r or x<r :
            ball['dx'] *=(-1)
            ball['dx'] += rnd(-1, 2)
    if y>600 - r or y<r:
            ball['dy'] *=(-1)
            ball['dy'] += rnd(-1, 2)
    
def mark(event): #куда попали мышкой; если попали на шарик, очки увеличиваются
        global points
        print(event.x, event.y)
        if ((event.x-x)**2+(event.y-y)**2) < (r**2):
                points+=1
                ball1 = new_ball()
                ball2 = new_ball()
        print(points)

balls = [new_ball() for i in range(10)]

update()

canv.bind('<Button-1>', mark)



mainloop() #запуск обработка главных событий
