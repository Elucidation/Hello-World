import random
from Environment import *
from Creature import *
import pickle

random.seed(2342040)


print "\n----- Running World Simulation -----\n"


        
#World = Environment()
if (raw_input("(l)oad world or (c)reate new world?: ")=='l'):
    with open("save/"+raw_input("Enter World name:")) as f:
        World = pickle.load(f)
else:
    World = Environment()
    for i in range(0,5):
        World.addCreature( randCreature() )



for i in range(0,200):
    World.step()


print "\n----- World Simulation Finished -----\n"
World.printStatus()

filename = "cWorld"+str(World.time)


print "\nSaving Current World to file " +filename+"..."
with open('save/'+filename,'w') as f:
    pickle.dump(World,f)
print "World saved."
