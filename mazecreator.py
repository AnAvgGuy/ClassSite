import pygame as py
import math as m
import json


screen = py.display.set_mode((1280,640))


#Values
START = 0
END = 1
SEARCHED = 2
UNSEARCHED = 3
WALL = 4

width, height = 160,80

grid = [[[x,y], UNSEARCHED, None, 0]  for y in range(height) for x in range(width)]

colors = {UNSEARCHED : (200,200,200),
          WALL: (80,80,80)}

fps = 60
click = 0
click2 = 0

file = open("data3.json", "r+")

grid = json.loads(file.read())

for i in range(0,len(grid)):
    if i < width or i > height*width-width-1 or i%width == 0 or (i%width) == width-1:
        grid[i][1] = WALL




clock = py.time.Clock()
run = 1
while run:
    screen.fill((0,0,0))

    for e in py.event.get():
        if e.type == py.QUIT:
            run = 0
        if e.type == py.MOUSEBUTTONDOWN:
            if e.button == 1:
                click = 1
            if e.button == 3:
                click2 = 1
        if e.type == py.MOUSEBUTTONUP:
            if e.button == 1:
                click = 0
            if e.button == 3:
                click2 = 0

    mox, moy = py.mouse.get_pos()      

    for i in grid:
        py.draw.rect(screen, colors[i[1]], ((i[0][0] * 1280/width, i[0][1] * 1280/width), (1280/width - 1, 640/height - 1)))

        if click:
            if int(mox/ (1280/width)) == i[0][0] and int(moy/ (1280/width)) == i[0][1]:
                i[1] = WALL
        if click2:
            if int(mox/ (1280/width)) == i[0][0] and int(moy/ (1280/width)) == i[0][1]:
                i[1] = UNSEARCHED


    clock.tick(fps)
    py.display.update()

file.close()

file = open("data3.json", "w")
file.close()

file = open("data3.json", "r+")
file.write(json.dumps(grid))

file.close()
