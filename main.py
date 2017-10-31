#! /usr/bin/env python3
# coding: utf-8

from classes import *
from constants import *

game_loop = 1

#Initialization of the lvl 
lvl = Map()
lvl.create()

#Initialization of the character
mcGyver = Character(lvl)
#Initialization of the objects 
ether = Object(lvl)
needle = Object(lvl)
plastic_tube = Object(lvl)

list_obj = [ether, needle, plastic_tube]
for i in list_obj:
    i.obj_position()
  
#Game loop
while game_loop:

    direction = input("Choose your direction (z, q, s, d): ")

    if direction == 'z':
        mcGyver.move('up')
    elif direction == 'q':
        mcGyver.move('left')
    elif direction == 's':
        mcGyver.move('down')
    elif direction == 'd':
        mcGyver.move('right')

    #test if you collect an object
    for a in list_obj:
        mcGyver.take_obj(a)



    #Update the position
    mcGyver.display_position()
    print("You have ", mcGyver.nb_object," objects")
    
    #test if the game is over
    if (lvl.structure[mcGyver.y][mcGyver.x] == 'a'):
        game_loop = 0

if mcGyver.nb_object == 3:
    print("Victory")
else:
    print("Defeat: You miss some Object")



 
