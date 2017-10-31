from constants import *
import random


#Class that generate the level
class Map:

    def __init__(self):
        
        self.file = 'lvl_design.txt'
        self.structure = 0

    #Generate a lvl from the file
    def create(self):

        with open(self.file,'r') as file:
            structure_file = []

            for lign in file:
                lign_lvl = []

                for caracter in lign:
                    if caracter != "\n":
                        lign_lvl.append(caracter)

                structure_file.append(lign_lvl)

            self.structure = structure_file
            

#Class that generate the character
class Character:

    def __init__(self, lvl):

        #Initialization of the position
        self.x = 0
        self.y = 0

        #LVL where the character is
        self.lvl = lvl

        #Number of object taken
        self.nb_object = 0

    #Character's deplacement
    def move(self, direction):

        if direction == 'right':
            # Test if the character will not go out of the screen
            if self.x < (side_sprite - 1):
                #Test if the destination is not a wall
                if self.lvl.structure[self.y][self.x + 1] != 'm':
                    #Incrementing self.x by 1
                    self.x += 1

        if direction == 'left':
            if self.x > 0:
                if self.lvl.structure[self.y][self.x - 1] != 'm':
                    self.x -= 1


        if direction == 'up':
            if self.y > 0:
                if self.lvl.structure[self.y - 1][self.x] != 'm':
                    self.y -= 1

        if direction == 'down':
            if self.y < (side_sprite - 1):
                #Test if the destination is not a wall
                if self.lvl.structure[self.y + 1][self.x] != 'm':
                    #Decrementing self.y by 1
                    self.y += 1


    #Print the position
    def display_position(self):
        
        print("x = ", self.x, "| y =", self.y)
    
    #Get the object
    def take_obj(self, obj):
        
        if (self.x == obj.obj_x) and (self.y == obj.obj_y):
            self.nb_object +=1
            obj.obj_x = 100
            obj.obj_y = 100
            

#Class that generate objects
class Object:

    #Create an object and place him in random position
    def __init__(self, lvl):

        self.obj_x = 0
        self.obj_y = 0
        self.lvl = lvl
        while self.lvl.structure[self.obj_y][self.obj_x] != 'o':
            self.obj_x = random.randint(0, 14)
            self.obj_y = random.randint(0, 14)


    #Get the object position
    def obj_position(self):
        print("coordonnées de l'objet : x = ", self.obj_x, "| y =", self.obj_y)
