from mcpi.minecraft import Minecraft as mc
mcs=mc.creater()
x,y,z=mcs.player.getTPos()
mc.setblack(x,y,z+1,68,2,"i love minecraft")