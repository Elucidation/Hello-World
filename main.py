import random
from Environment import Environment
from Creature import Creature

random.seed(2342040)

import randomName
print "\n-----Running World Simulation-----\n"


        
World = Environment()

for i in range(0,5):
    World.creatures.append(
        Creature(randomName.randShortName())
        )



for i in range(0,10):
    World.step()


print "\n-----World Simulation Finished-----\n"
World.printStatus()
