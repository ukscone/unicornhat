#!/usr/bin/env python

import unicornhat as unicorn
from PIL import ImageFont, ImageDraw, Image
import time, sys, getopt

unicorn.rotation(90)
unicorn.brightness(0.2)

str="*** Merry Christmas ***"
fore="red"
back="green"

def scroll(image):
    width,height = image.size
    for offset in range(0,width-8):
       for x in range(8):
        for y in range(8):
            r, g, b = image.getpixel((offset+x,y))
            unicorn.set_pixel(x, y, r,g,b)
       unicorn.show()
       time.sleep(0.3)


image = Image.new( 'RGB', (8*len(str),8), back)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("Beeb.ttf", 8)

draw.text((0, 0),str, font=font,fill=fore)

scroll(image)
