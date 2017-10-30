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
#Initialization of the objects with the method create_objects from the Object class
ether = Object(lvl)
needle = Object(lvl)
plastic_tube = Object(lvl)

list_obj = [ether, needle, plastic_tube]

#object counter
nb_object = 0
  
#Game loop
while game_loop:

    direction = input("Choose your direction (Z, Q, S, D): ")

    if direction == 'z':
        mcGyver.move('up')
    elif direction == 'q':
        mcGyver.move('left')
    elif direction == 's':
        mcGyver.move('down')
    elif direction == 'd':
        mcGyver.move('right')

    #test if you collect an object
    



    #Update the position
    mcGyver.display_position()
    print("You got ", nb_object," objects")
    
    #Victory test
    if (lvl.structure[mcGyver.y][mcGyver.x] == 'a'):
        game_loop = 0

print("Victory")
    



 
