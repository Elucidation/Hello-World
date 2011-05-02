print "Hello World!"

class Environment:
    "Where Creatures live, 2D plane 100x100 units starting from 0,0"
    def __init__(self):
        self.MAXWIDTH = 100
        self.MAXHEIGHT = 100
        self.creatures = []
    def step(self):
        for c in self.creatures:
            c.energy -= 1
        self.removeDead()
    def removeDead(self):
        for c in self.creatures:
            print "Checking if ",c," is dead... ",c.isDead()

class Creature:
    "It lives..."
    def __init__(self,name):
        self.name = name
        self.x = 0
        self.y = 0
        self.energy = 100
    def isDead(self):
        return self.energy <= 0
    def __str__(self):
        return self.name
        
World = Environment()

bubs = Creature("Bubs")

World.creatures.append(bubs)


World.step()
