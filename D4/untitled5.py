from mcpi.minecraft import Minecraft
from time import sleep
import random
mc=Minecraft.create ()
myID=mc.getPlayerEntityId("Weihan_Lai")
mineral=[14,15,16,56,73,129]
while True:
    sleep(0.5)
    r=random.choice(mineral)
    x,y,z=mc.entity.getTilePos(myID)
    mc.setBlocks(x+10,y,z,X-10,y,z,r)