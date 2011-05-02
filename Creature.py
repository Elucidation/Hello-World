import random
import randomName
class Creature:
    "It lives..."
    def __init__(self,name,x=0,y=0,energy=100,life=100):
        self.name = name
        self.x = x
        self.y = y
        self.birthday = -1
        self.deathday = -1
        self.energy = energy # if drops to zero is death
        self.life = life # This deteriorates at 1 per turn atm, can change
    def setBirth(self,time):
        self.birthday = time
    def changeEnergy(self,amount):
        self.energy += amount
        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100
    def changeLife(self,amount):
        self.life += amount
        if self.life < 0:
            self.life = 0
        elif self.life > 100:
            self.life = 100
    def canGiveBirth(self):
        return self.energy > 95
    def getPos(self):
        return self.x,self.y
    def setPos(self,x,y):
        self.x=x
        self.y=y
    def giveBirth(self):
        self.changeEnergy(-95)
        babyname = self.name
        bx = self.x + random.randrange(-10,10)
        by = self.y + random.randrange(-10,10)
        return Creature(babyname,bx,by)

    def kill(self,time):
        print self.name+" died at age "+`(time-self.birthday)`
        del(self)
    def isDead(self):
        return self.energy <= 0 or self.life <= 0
    def __str__(self):
        return self.name+ \
            "("+ \
            "L:"+`self.life`+","+\
            "E:"+`self.energy`+","+ \
            "P:(x:"+`self.x`+",y:"+`self.y`+")"+","+ \
            "Born:"+`self.birthday` + \
            ")"



def randCreature():
    x = random.randrange(10,90)
    y = random.randrange(10,90)
    name = randomName.randShortName()
    bob = Creature(name,x,y)
    return bob
