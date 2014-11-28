#!/usr/bin/env python

import unicornhat as unicorn
import getch, random, time, colorsys
import numpy as np

unicorn.rotation(90)
unicorn.brightness(0.4)

screen = [[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]

score=0
carX=3
carY=6

def drawObstacles():
    for y in range(8):
        for x in range(8):
            unicorn.set_pixel(x,y,0,screen[y][x],0)
    unicorn.show()

def addObstacle():
    r=random.randrange(0,abs(10-(score/10)))
    if r==1:
        screen[0][random.randrange(0,7)]=64

def moveObstacles():
    for y in range(7,-1,-1):
        for x in range(7):
            screen[y][x]=screen[y-1][x]

def drawCar(y, x):
    unicorn.set_pixel((x),(y),0,0,64 )
    unicorn.set_pixel((x)+1,(y),0,0,64 )
    unicorn.set_pixel((x),(y)+1,0,0,64 )
    unicorn.set_pixel((x)+1,(y)+1,0,0,64)
    unicorn.show()

def undrawCar(y,x):
    unicorn.set_pixel((x),(y),0,0,0)
    unicorn.set_pixel((x)+1,(y),0,0,0)
    unicorn.set_pixel((x),(y)+1,0,0,0)
    unicorn.set_pixel((x)+1,(y)+1,0,0,0)
    unicorn.show()

def checkHit():
    if (screen[carY][carX]==64) or (screen[carY+1][carX]==64) or (screen[carY][carX+1]==64) or (screen[carY+1][carX+1]==64):
        return True
    else:
        return False

def crashed():
    for z in range(10):
        rand_mat = np.random.rand(8,8)
        for y in range(8):
            for x in range(8):
                 h = 0.1 * rand_mat[x, y]
                 s = 0.8
                 v = rand_mat[x, y]
                 rgb = colorsys.hsv_to_rgb(h, s, v)
                 r = int(rgb[0]*255.0)
                 g = int(rgb[1]*255.0)
                 b = int(rgb[2]*255.0)
                 unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        time.sleep(0.01)

while True:
    moveObstacles()
    addObstacle()
    drawObstacles()
    drawCar(carY,carX)
    if (checkHit()==True):
        crashed()
        print "Crashed\nGame Over\nScore: ",score
        break
    else:
        score=score+1
        user_input=""
        while user_input=="":
            user_input = getch.getch().lower()
            if (user_input!="q") and (user_input!="w") and (user_input!=" ") and (user_input!="x"):
                user_input=""
        if user_input!="x":
            undrawCar(carY,carX)
            if user_input=="q":
                carX=carX-1
                if carX < 0:
                    carX=0
            elif user_input=="w":
                carX=carX+1
                if carX > 6:
                    carX=6
            elif user_input==" ":
                pass
        else:
           print "Game Over\nScore: ", score
           break
