import random
from Environment import *
from Creature import *
import pickle

random.seed(2342040)
filePrefix = "cBigWorld"

print "\n----- Running World Simulation -----\n"


        
#World = Environment()
if (raw_input("(l)oad world or (c)reate new world?: ")=='l'):
    with open("save/"+raw_input("Enter World name:")) as f:
        World = pickle.load(f)
        print "World Loaded..."
else:
    World = Environment()
    for i in range(0,100):
        World.addCreature( randCreature() )
    print "Creatures Created..."
    filename = filePrefix+"0"
    print "\nSaving New World to file " +filename+"..."
    with open('save/'+filename,'w') as f:
        pickle.dump(World,f)
        print "World saved to file..."



World.printStatus()
print "\n----- World Simulation Starting -----\n"


for i in range(0,1000):
    World.step()


print "\n----- World Simulation Finished -----\n"
World.printStatus()

filename = filePrefix+str(World.time)

print "\nSaving Current World to file " +filename+"..."
with open('save/'+filename,'w') as f:
    pickle.dump(World,f)
print "World saved."
