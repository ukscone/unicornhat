#!/usr/bin/env python

# 2048 code originally from http://www.thetaranights.com/make-a-2048-game-in-python/
# there is a bug/missing logic that needs to be fixed where it will quit the game
# even if there is still a valid move left when the grid is completely full.
# but other than that it works.  
 
import unicornhat as unicorn
import getch, random

unicorn.rotation(90)
unicorn.brightness(0.4)

grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

index = {0:0,2:1,4:2,8:3,16:4,32:5,64:6,128:7,256:8,512:9,1024:10,2048:11}
colour=((0,0,0),(0,127,0),(0,255,0),(0,0,127),(0,0,255),(127,0,0),(255,0,0),
        (127,127,0),(127,127,127),(255,127,127),(255,255,127),(255,255,255))

def drawTile(y, x, value):
    rgb=colour[(index[value])]
    unicorn.set_pixel((x*2),(y*2),rgb[0],rgb[1],rgb[2])
    unicorn.set_pixel((x*2)+1,(y*2),rgb[0],rgb[1],rgb[2])
    unicorn.set_pixel((x*2),(y*2)+1,rgb[0],rgb[1],rgb[2])
    unicorn.set_pixel((x*2)+1,(y*2)+1,rgb[0],rgb[1],rgb[2])
    unicorn.show()

def updateGrid(keypressed):
    if keypressed == "u":
        row=0
        for column in range(0,4):
            if grid[row][column]!=0 or grid[row+1][column]!=0 or grid[row+2][column]!=0 or grid[row+3][column]!=0:
                if grid[row][column]==0:
                    while grid[row][column]==0:
                        grid[row][column]=grid[row+1][column]
                        grid[row+1][column]=grid[row+2][column]
                        grid[row+2][column]=grid[row+3][column]
                        grid[row+3][column]=0
                if grid[row+1][column]==0 and (grid[row+2][column]!=0 or grid[row+3][column]!=0):
                    while grid[row+1][column]==0:
                        
                        grid[row+1][column]=grid[row+2][column]
                        grid[row+2][column]=grid[row+3][column]
                        grid[row+3][column]=0
                if grid[row+2][column]==0 and (grid[row+3][column]!=0):
                    while grid[row+2][column]==0:
                        grid[row+2][column]=grid[row+3][column]
                        grid[row+3][column]=0
        row=0
        for column in range(0,4):
            if grid[row][column]==grid[row+1][column]:
                grid[row][column]=grid[row][column]+grid[row+1][column]
                grid[row+1][column]=grid[row+2][column]
                grid[row+2][column]=grid[row+3][column]
                grid[row+3][column]=0
            if grid[row+1][column]==grid[row+2][column]:
                grid[row+1][column]=grid[row+1][column]+grid[row+2][column]
                grid[row+2][column]=grid[row+3][column]
                grid[row+3][column]=0
            if grid[row+2][column]==grid[row+3][column]:
                grid[row+2][column]=grid[row+2][column]+grid[row+3][column]
                grid[row+3][column]=0
                        
                        
          
    elif keypressed == "d":
        row=0
        for column in range(0,4):
            if grid[row][column]!=0 or grid[row+1][column]!=0 or grid[row+2][column]!=0 or grid[row+3][column]!=0:
                if grid[row+3][column]==0:
                    while grid[row+3][column]==0:
                        grid[row+3][column]=grid[row+2][column]
                        grid[row+2][column]=grid[row+1][column]
                        grid[row+1][column]=grid[row][column]
                        grid[row][column]=0
                if grid[row+2][column]==0 and (grid[row+1][column]!=0 or grid[row][column]!=0):
                    while grid[row+2][column]==0:
                        grid[row+2][column]=grid[row+1][column]
                        grid[row+1][column]=grid[row][column]
                        grid[row][column]=0

                if grid[row+1][column]==0 and grid[row][column]!=0:
                    while grid[row+1][column]==0:
                        grid[row+1][column]=grid[row][column]
                        grid[row][column]=0
        row=0
        for column in range(0,4):
            if grid[row+3][column]==grid[row+2][column]:
                grid[row+3][column]=grid[row+3][column] + grid[row+2][column]
                grid[row+2][column]=grid[row+1][column]
                grid[row+1][column]=grid[row][column]
                grid[row][column]=0
            if grid[row+2][column]==grid[row+1][column]:
                grid[row+2][column]=grid[row+2][column]+grid[row+1][column]
                grid[row+1][column]=grid[row][column]
                grid[row][column]=0
            if grid[row+1][column]==grid[row][column]:
                grid[row+1][column]=grid[row+1][column]+grid[row][column]
                grid[row][column]=0
            
    elif keypressed == "l":
        column=0
        for row in range(0,4):

            if grid[row][column]!=0 or grid[row][column+1]!=0 or grid[row][column+2]!=0 or grid[row][column+3]!=0:
                if grid[row][column]==0:
                    while grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=grid[row][column+2]
                        grid[row][column+2] = grid[row][column+3]
                        grid[row][column+3]=0
                if grid[row][column+1]==0 and (grid[row][column+2]!=0 or grid[row][column+3]!=0):
                    while grid[row][column+1]==0:
                        grid[row][column+1]=grid[row][column+2]
                        grid[row][column+2]=grid[row][column+3]
                        grid[row][column+3]=0
                if grid[row][column+2]==0 and (grid[row][column+3]!=0):
                    while grid[row][column+2]==0:
                        grid[row][column+2]=grid[row][column+3]
                        grid[row][column+3]=0
        column=0
        for row in range(0,4):
            if grid[row][column]==grid[row][column+1]:
                grid[row][column]=grid[row][column]+grid[row][column+1]
                grid[row][column+1]=grid[row][column+2]
                grid[row][column+2]=grid[row][column+3]
                grid[row][column+3]=0
            if grid[row][column+1]==grid[row][column+2]:
                grid[row][column+1]=grid[row][column+1]+grid[row][column+2]
                grid[row][column+2]=grid[row][column+3]
                grid[row][column+3]=0
            if grid[row][column+2]==grid[row][column+3]:
                grid[row][column+2]=grid[row][column+2]+grid[row][column+3]
                grid[row][column+3]=0
    elif keypressed == "r":
        column=0
        for row in range(0,4):
            if grid[row][column]!=0 or grid[row][column+1]!=0 or grid[row][column+2]!=0 or grid[row][column+3]!=0:
                if grid[row][column+3]==0:
                    while grid[row][column+3]==0:
                        grid[row][column+3]=grid[row][column+2]
                        grid[row][column+2]=grid[row][column+1]
                        grid[row][column+1]=grid[row][column]
                        grid[row][column]=0
                if grid[row][column+2]==0 and (grid[row][column+1]!=0 or grid[row][column]!=0):
                    while grid[row][column+2]==0:
                        grid[row][column+2]=grid[row][column+1]
                        grid[row][column+1]=grid[row][column]
                        grid[row][column]=0

                if grid[row][column+1]==0 and grid[row][column]!=0:
                    while grid[row][column+1]==0:
                        grid[row][column+1]=grid[row][column]
                        grid[row][column]=0
        column=0
        for row in range(0,4):
            if grid[row][column+3]==grid[row][column+2]:
                grid[row][column+3]=grid[row][column+3] + grid[row][column+2]
                grid[row][column+2]=grid[row][column+1]
                grid[row][column+1]=grid[row][column]
                grid[row][column]=0
            if grid[row][column+2]==grid[row][column+1]:
                grid[row][column+2]=grid[row][column+2]+grid[row][column+1]
                grid[row][column+1]=grid[row][column]
                grid[row][column]=0
            if grid[row][column+1]==grid[row][column]:
                grid[row][column+1]=grid[row][column+1]+grid[row][column]
                grid[row][column]=0
        

grid[random.choice([0,1,2,3])][random.choice([0,1,2,3])]=2
                
while True:
    for y in range(4):
        for x in range(4):
           drawTile(y,x,grid[y][x])

    keypressed=""
    while keypressed=="":
        keypressed = getch.getch().lower()
        if (keypressed!="u") and (keypressed!="d") and (keypressed!="l") and (keypressed!="r") and (keypressed!="q"):
            keypressed=""

    if keypressed!="q":
        updateGrid(keypressed)
        listForRow = []
        listForColumnn = []
        count = 0
        for row in range(0,4):
            for column in range(0,4):
                if grid[row][column]==0:
                    count+=1
                    listForRow.append(row)
                    listForColumnn.append(column)
        if count > 0:
            if count > 1:
                randomIndex = listForRow.index(random.choice(listForRow))
                grid[listForRow[randomIndex]][listForColumnn[randomIndex]]=2
            else:
                grid[listForRow[0]][listForColumnn[0]]=2
        else:
            break
    else:
        break
print "Game over"
