from mcpi.minecraft import Minecraft as mc
mcs=mc.creater()
userName=input("What/'s your name?")
message=("What/'s your message?")
mcs.postToChat("["+userName"]"+message)