#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicornhat as unicorn
import time, sys, getopt, webcolors

from font import font
from icons import icon

unicorn.rotation(90)
unicorn.brightness(0.18)
delay=0.05

palette={0:webcolors.name_to_rgb('red'),
         1:webcolors.name_to_rgb('orange'),
         2:webcolors.name_to_rgb('yellow'),
         3:webcolors.name_to_rgb('green'),
         4:webcolors.name_to_rgb('blue'),
         5:webcolors.name_to_rgb('indigo'),
         6:webcolors.name_to_rgb('violet'),
         7:webcolors.name_to_rgb('lightslategray')}

outer_border  = webcolors.name_to_rgb('red')
middle_border = webcolors.name_to_rgb('green')
inner_border  = webcolors.name_to_rgb('blue')
centre        = webcolors.name_to_rgb('white')

attrib = [
[outer_border,   outer_border,  outer_border,  outer_border,  outer_border,  outer_border,  outer_border, outer_border],
[outer_border,  middle_border, middle_border, middle_border, middle_border, middle_border, middle_border, outer_border], 
[outer_border,  middle_border,  inner_border,  inner_border,  inner_border,  inner_border, middle_border, outer_border],
[outer_border,  middle_border,  inner_border,        centre,        centre,  inner_border, middle_border, outer_border], 
[outer_border,  middle_border,  inner_border,        centre,        centre,  inner_border, middle_border, outer_border], 
[outer_border,  middle_border,  inner_border,  inner_border,  inner_border,  inner_border, middle_border, outer_border], 
[outer_border,  middle_border, middle_border, middle_border, middle_border, middle_border, middle_border, outer_border], 
[outer_border,   outer_border,  outer_border,  outer_border,  outer_border,  outer_border,  outer_border, outer_border]]


def rotate_string(text,mode=1,steps=1):
    length=len(text)
    for step in range(steps):
        if mode==0:
            text=text[length-1] + text[0:length-1]
        else:
            text=text[1:length] + text[0]
    return text

def message_to_bitmap(message):
    bitmap=["" for y in range(8)]
    for z in range(len(message)):
        character=ord(message[z])-32
        for y in range(8): 
            bitmap[y]+=font[character][y]
    return bitmap

def add_icon_to_bitmap(image, bitmap):
    for y in range(8):
        bitmap[y]+=icon[image][y]
    return bitmap

def setpixel(x,y,mode):
    if type(mode)==str:
        if mode=="attrib":
            unicorn.set_pixel(x,y,attrib[x][y][0],attrib[x][y][1],attrib[x][y][2])
        elif mode=="palette_column":
            unicorn.set_pixel(x,y,palette[x][0],palette[x][1],palette[x][2])
        elif mode=="palette_row":
            unicorn.set_pixel(x,y,palette[y][0],palette[y][1],palette[y][2])
    elif type(mode)==tuple:
        unicorn.set_pixel(x,y,mode[0],mode[1],mode[2])
    else:
        unicorn.set_pixel(x,y,255,255,255)

def test():
    bitmap=message_to_bitmap("Test ")
    bitmap=add_icon_to_bitmap('smile',bitmap) 
    bitmap_len=len(bitmap[0])
    count=0
    while True:
        while count < bitmap_len:
            for y in range(8):
                for x in range(8):
                    if bitmap[y][x]=="#":
                        setpixel(x,y,"attrib")
                    else:
                        unicorn.set_pixel(x,y,0,0,0)
            unicorn.show()
            time.sleep(delay)
            for y in range(8):
                bitmap[y]=rotate_string(bitmap[y],1,1)
            count+=1
        count=0
        while count < bitmap_len:
            for y in range(8):
                for x in range(8):
                    if bitmap[y][x]=="#":
                        setpixel(x,y,"attrib")
                    else:
                        unicorn.set_pixel(x,y,0,0,0)
            unicorn.show()
            time.sleep(delay*8)
            for y in range(8):
                bitmap[y]=rotate_string(bitmap[y],1,8)
            count+=8
        count=0

if __name__ == "__main__":
   test()
