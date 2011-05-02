import random
from Environment import *
from Creature import *


random.seed(2342040)


print "\n----- Running World Simulation -----\n"


        
World = Environment()


    

for i in range(0,5):
    World.addCreature( randCreature() )



for i in range(0,30):
    World.step()


print "\n----- World Simulation Finished -----\n"
World.printStatus()
