from constants import *

#class that generate the level
class Map:

    def __init__(self, file):
        
        self.file = file
        self.structure = 0

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
                

#class that generate the character
class Character:

    def __init__(self, lvl):

        #Initialization of the position
        self.x = 0
        self.y = 0

        #LVL where the character is
        self.lvl = lvl


    def move(self, direction):

        if direction == 'right':
            # Test if the character will not go out of the screen
            if self.x < (side_sprite - 1):
                #Test if the destination is not a wall
                if self.lvl.structure[self.y][self.x + 1] != 'm':
                    #Incrementing self.x by 1
                    self.x += 1

        if direction == 'left':
            # Test if the character will not go out of the screen
            if self.x > 0:
                #Test if the destination is not a wall
                if self.lvl.structure[self.y][self.x - 1] != 'm':
                    #Decrementing self.x by 1
                    self.x -= 1


        if direction == 'up':
            # Test if the character will not go out of the screen
            if self.y > 0:
                #Test if the destination is not a wall
                if self.lvl.structure[self.y - 1][self.x] != 'm':
                    #Incrementing self.y by 1
                    self.y -= 1

        if direction == 'down':
            if self.y < (side_sprite - 1):
                #Test if the destination is not a wall
                if self.lvl.structure[self.y + 1][self.x] != 'm':
                    #Decrementing self.y by 1
                    self.y += 1


    def display_position(self):
        print("x = ", self.x, "| y =", self.y)
    

#class that generate objects
class Object:

    def __init__(self):
        pass

    def create_objects(self):
        pass

    def remaining_objects(self):
        pass
