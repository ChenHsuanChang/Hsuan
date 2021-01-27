# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.gettilepos
while True:
    mcs.postTochat("you are located on X:"+str(x)+\
                   ',y:'+str(y)+"+str(z))
