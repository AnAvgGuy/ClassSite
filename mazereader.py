import pygame as py
import math as m
import json
import mazegenerator

screen = py.display.set_mode((1280,640))


#Values
START = 0
END = 1
SEARCHED = 2
UNSEARCHED = 3
WALL = 4


fps = 60
click = 0
click2 = 0

img = py.image.load("images.png")
img = py.transform.scale(img,(640,640))


clock = py.time.Clock()
run = 1
while run:
    screen.fill((0,0,0))
    screen.blit(img, (0,0))

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

    clock.tick(fps)
    py.display.update()