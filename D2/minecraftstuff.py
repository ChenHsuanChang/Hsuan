# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft as mc
import time
time.sleep(2)
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
s=100
mcs.setBlocks(x-s,y,z-s,x+s,y+s,z+s,0)
