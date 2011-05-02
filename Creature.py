import random
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
