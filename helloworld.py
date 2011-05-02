import random

random.seed(2342040)

import randomName
print "Hello World!"

class Environment:
    "Where Creatures live, 2D plane 100x100 units starting from 0,0"
    def __init__(self):
        self.MAXWIDTH = 100
        self.MAXHEIGHT = 100
        self.creatures = []
        self.time = 0
        
    def step(self):
        self.time += 1
        self.printStatus()
        print "-----Stepping-----"
        for c in self.creatures:
            c.energy -= 1
        self.removeDead()

    def removeDead(self):
        for c in self.creatures:
            print "Checking if ",c," is dead... ",c.isDead()

    def printStatus(self):
        print "------Environment------"
        print " Time: ", self.time, " units"
        print " Population Count: ", len(self.creatures)

class Creature:
    "It lives..."
    def __init__(self,name):
        self.name = name
        self.x = 0
        self.y = 0
        self.energy = 3 + random.randrange(0,5)
    def isDead(self):
        return self.energy <= 0
    def __str__(self):
        return self.name+"(E:"+`self.energy`+")"
        
World = Environment()

for i in range(0,5):
    World.creatures.append(
        Creature(randomName.randShortName())
        )



for i in range(0,10):
    World.step()
