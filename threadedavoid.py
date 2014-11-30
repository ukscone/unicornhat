#!/usr/bin/env python

import unicornhat as unicorn
import random, time, colorsys, threading
import numpy as np

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

old_settings=''
fd=''
def readchar():
    global old_settings
    global fd
    fd = sys.stdin.fileno()

    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

unicorn.rotation(90)
unicorn.brightness(0.4)

road = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]


carX=0
carY=6
score=0
crashed=False

class obstacles(threading.Thread):

    def __init__(self):
        self._stopevent = threading.Event( )
        self._sleepperiod = 0.5
        threading.Thread.__init__(self)

    def run(self):
      global crashed
      while not self._stopevent.isSet( ):
          self.move()
          self.check()
          self.add()
          self.draw()
          self._stopevent.wait(self._sleepperiod)

    def join(self, timeout=None):
          self._stopevent.set( )
          threading.Thread.join(self, timeout)

    def draw(self):
        for y in range(8):
            for x in range(8):
                unicorn.set_pixel(x,y,0,road[y][x],0)
        unicorn.set_pixel((carX),(carY),0,0,64 )
        unicorn.set_pixel((carX)+1,(carY),0,0,64 )
        unicorn.set_pixel((carX),(carY)+1,0,0,64 )
        unicorn.set_pixel((carX)+1,(carY)+1,0,0,64)

        unicorn.show()

    def add(self):
        r=random.randrange(0,5)#(10-abs(score/10)))
        if r==1:
            road[0][random.randrange(0,8)]=64

    def move(self):
        for y in range(7,-1,-1):
            for x in range(8):
                road[y][x]=road[y-1][x]

    def crash(self):
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


    def check(self,timeout=None):
        global carX
        global carY
        global crashed
        global score
        global old_settings
        global fd
        if (road[carY][carX]==64) or (road[carY+1][carX]==64) or (road[carY][carX+1]==64) or (road[carY+1][carX+1]==64):
            self.crash()
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            print "Game Over\nCrashed"
            print "Score", score
            print "Press enter key to exit"
            self._stopevent.set( )
            crashed=True
        else:
          score=score+1


thread1=obstacles()
thread1.daemon = True
thread1.start()

while True:
    if crashed==True:
      break
    user_input = readkey()
    if user_input=='q':
       carX=carX-1
       if carX < 0:
           carX=0
    elif user_input=='w':
        carX=carX+1
        if carX > 6:
             carX=6
    elif user_input=='x':
        print "exiting"
        break
    elif user_input=='t':
        thread1.join() 
    else:
        pass
