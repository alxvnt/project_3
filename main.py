#! /usr/bin/env python3
# coding: utf-8

from classes import *
from constants import *

game_loop = 1


    



#Initialization of the lvl 
lvl = Map('lvl_design.txt')
lvl.create()

#Initialization of the character
McGyver = Character(lvl)
#Initialization of the objects with the method create_objects from the Object class
    
#Game loop
while game_loop:

    direction = input("Entrez votre direction (Z, Q, S, D): ")

    if direction == 'z':
        McGyver.move('up')
    elif direction == 'q':
        McGyver.move('left')
    elif direction == 's':
        McGyver.move('down')
    elif direction == 'd':
        McGyver.move('right')


    #Update the position
    McGyver.display_position()
    
    #Victory test
    if lvl.structure[McGyver.y][McGyver.x] == 'a':
        game_loop = 0

print("Victory")
    



 
