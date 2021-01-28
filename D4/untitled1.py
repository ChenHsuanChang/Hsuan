from mcpi.minecraft import Minecraft
mc=Minecraft.create ()
x,y,z=mc.player.getTilePos()
number=10
for i in range(8):
    for i in range(number):
        mc.spawnEntity(x,y,z,63)
    number=number*20
    mc.postToChat("生成了"+(number)+"FISH")