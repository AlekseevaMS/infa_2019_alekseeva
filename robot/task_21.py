#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n=12
    m=10
    move_right()
    move_down()
    for i in range(0,4):
        for j in range(0, n):
            fill_cell()
            move_down()
            fill_cell()
            move_right()
        n-=3
        fill_cell()
        move_left(n=2)
        for j in range(0, m):
            fill_cell()
            move_left()
            fill_cell()
            move_up()
        m-=3
        fill_cell()
        move_down()
    move_down()

if __name__ == '__main__':
    run_tasks()
