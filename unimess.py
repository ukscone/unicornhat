#!/usr/bin/env python

import unicornhat as unicorn
from PIL import Image
import sys, signal, numpy, time

unicorn.rotation(90)
unicorn.brightness(0.09)

def drawChar(offset_y, offset_x):
    for x in range(7,-1,-1):
        for y in range(8):
            pixel = img.getpixel(((offset_x*8)+x,(offset_y*8)+y))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    time.sleep(0.5)

def findOffset(character):
    row=(ord(character)/32)-1
    if ord(character) >= 97:
        column=ord(character)-97
    elif ord(character) >= 65:
        column=ord(character)-65
    else:
        column=ord(character)-33
    return (row, column)

img = Image.open('font.png')
message=sys.stdin.readlines()
for line in range(len(message)):
  for char in range(len(message[line])):
    if (message[line][char]!=' ') and (message[line][char]!='\n'):
        row, column=findOffset(message[line][char])
        drawChar(row,column)
    else:
        unicorn.off()
        time.sleep(0.5)
