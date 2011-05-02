print "Hello World!"

class Environment:
    "Where Creatures live, 2D plane 100x100 units starting from 0,0"
    def __init__(self):
        self.MAXWIDTH = 100
        self.MAXHEIGHT = 100
        self.creatures = []

class Creature:
    "It lives..."
    def __init__(self):
        self.x = 0
        self.y = 0
        self.energy = 100
        
World = Environment()

bubs = Creature()

World.creatures.append(bubs)
