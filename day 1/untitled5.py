
from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.gettilepose
mcs.setblock(x+1,y,z,15)
mcs.setblock(x-1,y,z,15)
mcs.setblock(x-1,y,z-1,15)
