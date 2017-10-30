

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

    def __init__(self):

        #Initialization of the position
        self.x = 0
        self.y = 0

    def move(self):
        pass

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
