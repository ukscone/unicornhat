#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicornhat as unicorn
import time, webcolors

from font import font
from icons import icon

unicorn.rotation(90)
unicorn.brightness(0.2)

column1= webcolors.name_to_rgb('red')
column2= webcolors.name_to_rgb('blue')
column3= webcolors.name_to_rgb('pink')
column4= webcolors.name_to_rgb('green')
column5= webcolors.name_to_rgb('yellow')
column6= webcolors.name_to_rgb('white')
column7= webcolors.name_to_rgb('purple')
column8= webcolors.name_to_rgb('cyan')

cols=[
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8],
[column1,column2,column3,column4,column5,column6,column7,column8]]


class Message():
    def __init__(self):
        self.bitmap    = ["" for rows in range(8)]
#        self.attributes = [[] for rows in range(8)]
         
    def add_text(self, message):
        for z in range(len(message)):
            character=ord(message[z])-32
            for y in range(8):
                self.bitmap[y]+=font[character][y]

    def add_graphic(self, image):
        for y in range(8):
            self.bitmap[y]+=icon[image][y]

    def clear(self):
        self.bitmap    = ["" for rows in range(8)]
#        self.attributes = [[] for rows in range(8)]

    def rotate_bitmap(self,mode=1,steps=1):
        for row in range(8):
            length=len(self.bitmap[row])
            for step in range(steps):
                if mode==0:
                    self.bitmap[row]=self.bitmap[row][-1] + self.bitmap[row][:-1]
                else:
                    self.bitmap[row]=self.bitmap[row][1:] + self.bitmap[row][0:1]

    def scroll(self,attributes=(255,255,255),direction=1, steps=1, delay=0.05):
        while True:
            for y in range(8):
                for x in range(8):
                     if self.bitmap[y][x]=="#":
                         self.setpixel(x,y,attributes)
                     else:
                         unicorn.set_pixel(x,y,0,0,0)
            unicorn.show()
            time.sleep(delay)
            self.rotate_bitmap(direction,steps)


    def setpixel(self,x,y,attributes=(255,255,255)):
        if type(attributes)==list:
            unicorn.set_pixel(x,y,attributes[y][x][0],attributes[y][x][1],attributes[y][x][2])
        elif type(attributes)==tuple:
            unicorn.set_pixel(x,y,attributes[0],attributes[1],attributes[2])

#
#def rotate(attrib,mode=1,steps=1):
#    for row in range(8):
#         for step in range(steps):
#             if mode==0:
#                 attrib[row]=attrib[row][-1:] + attrib[row][:-1]
#             else:
#                 attrib[row]=attrib[row][1:] + attrib[row][0:1]

message=Message()
message.add_graphic('xmastree')
message.add_text(" Merry Christmas ")
message.add_graphic('xmastree')
message.add_text("Happy New Year")
message.scroll(cols)
