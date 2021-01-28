from mcpi.minecraft import Minecraft
from random import randint
import time
mc=Minecraft.create ()
x,y,z=mc.player.getTilePos()
color=randint(0,15)
c=5
for i in range(20):
    for j in range(20):
        color=randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==com:
           mc.postToChat(Win)
           break
        else:
           mc.postToChat("you have"+str(c))
           c=c-1
    if c==-1:
        mc.postToChat(Loser)