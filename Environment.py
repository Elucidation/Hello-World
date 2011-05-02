import random

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
        print "Test"
        print " Time: ", self.time, " units"
        print " Population Count: ", len(self.creatures)


