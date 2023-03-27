import pygame as py
import math as m
import json
import colorsys


screen = py.display.set_mode((1280,640))

py.font.init()
font = py.font.SysFont("TimesNewRoman", 16)

#Values
START = 0
END = 1
SEARCHED = 2
UNSEARCHED = 3
WALL = 4
PRESEARCHED = 5
INPATH = 6

width, height = 160,80


def color_func(val):
    val = min(200,val)
    val = max(0,val)
    blue = val
    green = val/2
    red = 200-val
    return (red, green, blue)

def rainbow_func(val):
    r,g,b = (colorsys.hsv_to_rgb(val/200,1,1))
    return r * 255, g * 255, b * 255

colors = {UNSEARCHED : (200,200,200),
          WALL: (80,80,80),
          START : (0,200,0),
          END : (26,26,26),
          SEARCHED : (100,100,200),
          PRESEARCHED : (235,170,40),
          INPATH : (255,255,255)}


file = open("data3.json", "r")
grid = json.loads(file.read())

grid[width+1][1] = START
grid[width*height - width - 2][1] = END

fps = 30
go = 0

clock = py.time.Clock()
run = 1
while run:
    screen.fill((0,0,0))

    for e in py.event.get():
        if e.type == py.QUIT:
            run = 0
        if e.type == py.MOUSEBUTTONDOWN:
            if e.button == 3:
                go = 1
    if go:
        idx = 0
        for i in grid:
            
            if i[1] == SEARCHED:
                py.draw.rect(screen, color_func(200-i[3]/2), ((i[0][0] * 1280/width, i[0][1] * 1280/width), (1280/width - 1, 640/height - 1)))
            else:
                py.draw.rect(screen, colors[i[1]], ((i[0][0] * 1280/width, i[0][1] * 1280/width), (1280/width - 1, 640/height - 1)))

            #screen.blit(font.render(str(i[3]),True,(0,0,0)), (i[0][0] * 1280/width, i[0][1] * 1280/width))

            if i[1] == START or i[1] == SEARCHED:
                if grid[idx+1][1] == UNSEARCHED:
                    grid[idx+1][1] = PRESEARCHED
                    grid[idx+1][2] = i
                    grid[idx+1][3] = i[3]+1
                if grid[idx-1][1] == UNSEARCHED:
                    grid[idx-1][1] = PRESEARCHED
                    grid[idx-1][2] = i
                    grid[idx-1][3] = i[3]+1
                if grid[idx+width][1] == UNSEARCHED:
                    grid[idx+width][1] = PRESEARCHED
                    grid[idx+width][2] = i
                    grid[idx+width][3] = i[3]+1
                if grid[idx-width][1] == UNSEARCHED:
                    grid[idx-width][1] = PRESEARCHED
                    grid[idx-width][2] = i
                    grid[idx-width][3] = i[3]+1

                closest = 10000
                closest_one = None
                if grid[idx+1][1] == END:
                    if grid[idx+1][3] < closest:
                        closest_one = idx+1
                        closest = grid[idx+1][3] 

                if grid[idx-1][1] == END:
                    if grid[idx-1][3] < closest:
                        closest_one = idx-1
                        closest = grid[idx-1][3]   
            
                if grid[idx+width][1] == END:
                    if grid[idx+width][3] < closest:
                        closest_one = idx+width
                        closest = grid[idx+width][3] 

                if grid[idx-width][1] == END:
                    if grid[idx-width][3] < closest:
                        closest_one = idx-width
                        closest = grid[idx-width][3] 

                if closest_one != None and grid[closest_one][2] == None:
                    grid[closest_one][2] = i

        
            if (i[1] == END or i[1] == INPATH) and i[2] != None and i[2] != "dontuse":
                i[2][1] = INPATH
                i[2] = "dontuse"


            idx += 1

        for i in grid:
            if i[1] == PRESEARCHED:
                i[1] = SEARCHED


    clock.tick(fps)
    py.display.update()

file.close()