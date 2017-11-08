#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

# Ouverture de la fenêtre Pygame
window = pygame.display.set_mode((window_size, window_size))

# Chargement et collage du fond
fond = pygame.image.load("pic/background.jpg").convert()


pygame.display.set_caption("Maze of Mac Gyver")


# BOUCLE PROG
prog = 1

# BOUCLE Jeu
continuer = 1


while prog:


        lvl = Map()
        lvl.create()
        lvl.display(window)
        mcGyver  = Character(mcGyver_right, mcGyver_left,mcGyver_up,mcGyver_down,lvl)

        nb_object = 0

        ether = Object(lvl, pic_ether)
        needle = Object(lvl, pic_needle)
        tube = Object(lvl, pic_tube)
        obj_list = [ether, needle, tube]

        
        while continuer:
                
                pygame.time.Clock().tick(30)

                for event in pygame.event.get():

                        if event.type == KEYDOWN:
                                if event.key == K_RIGHT:
                                        mcGyver.move('right')
                                elif event.key == K_LEFT:
                                        mcGyver.move('left')
                                elif event.key == K_UP:
                                        mcGyver.move('up')
                                elif event.key == K_DOWN:
                                        mcGyver.move('down')
                        

                window.blit(fond, (0,0))
                lvl.display(window)
                for obj in obj_list:
                        window.blit(obj.design, (obj.obj_sprite_x, obj.obj_sprite_y))
                        if obj.taken == False:
                                mcGyver.take_obj(obj)
                                #print(obj.taken)
                                
                print("You have ", mcGyver.nb_object," objects")
                window.blit(mcGyver.direction, (mcGyver.sprite_x, mcGyver.sprite_y))
                pygame.display.flip()

                if (lvl.structure[mcGyver.y][mcGyver.x] == 'a'):
                        continuer = 0

                        if mcGyver.nb_object == 3:
                                fond2 = pygame.image.load(victory).convert()
                        else:
                                fond2 = pygame.image.load(defeat).convert()
            
        window.blit(fond2, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
                if event.type == QUIT:
                        prog =0
                elif event.type == KEYDOWN:
                      if event.key == K_r:
                              continuer = 1
        
