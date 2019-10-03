#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while(not(wall_is_on_the_right())):
        if (not(wall_is_above()))and(wall_is_beneath()):
            while not(wall_is_above()):
                move_up()
                fill_cell()
            while not(wall_is_beneath()):
                move_down()
        move_right()
    if (wall_is_on_the_right())and(not(wall_is_above())):
        while not(wall_is_above()):
            move_up()
            fill_cell()
        while not(wall_is_beneath()):
            move_down()
    while wall_is_beneath():
        move_left()
        
        


if __name__ == '__main__':
    run_tasks()
