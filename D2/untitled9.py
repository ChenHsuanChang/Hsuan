from mcpi.minecraft import Minecraft as mc
import time
time.sleep(2)
mcs=mc.create()
while True:
     x,y,z=mcs.player.getPos()
     mcs.setBlock(x,y+2,z,11)
     time.sleep(1)
     