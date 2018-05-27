#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint

mc = Minecraft.create()

height = 40

x,y,z = mc.player.getTilePos()
treeX = x + 25
treeZ = z
treeY = mc.getHeight(treeX, treeZ)

# During test / development we will restore the world.
mc.saveCheckpoint()

# Main trunk.
mc.setBlocks(treeX, treeY, treeZ, treeX, treeY+height, treeZ, block.WOOD.id)
mc.setBlock(treeX, treeY+height, treeZ, block.DIAMOND_BLOCK.id)

# Main branches.
for i in range(treeY+2, treeY+height, 3):
    length = int((height - i) *0.6)

    # Add the North facing branch.
    mc.setBlocks(treeX, i, treeZ, treeX+length, i, treeZ, block.LEAVES.id)

    # Add fairy lights to some branches.
    if (randint(0,1) == 1):
        mc.setBlock(treeX+length, i+1, treeZ, block.GLOWING_OBSIDIAN.id)

    # Add Sub-branches either side.
    for j in range(0, length, 3):
        length2 = int((length-j) *0.75)
        mc.setBlocks(treeX+j, i, treeZ, treeX+j, i, treeZ+length2, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX+j, i-1, treeZ+length2, block.WOOL.id, randint(1,14))
        mc.setBlocks(treeX+j, i, treeZ, treeX+j, i, treeZ-length2, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX+j, i-1, treeZ-length2, block.WOOL.id, randint(1,14))
 
    # Add the South facing branch.
    mc.setBlocks(treeX, i, treeZ, treeX-length, i, treeZ, block.LEAVES.id)

    # Add fairy lights to some branches.
    if (randint(0,1) == 1):
        mc.setBlock(treeX-length, i+1, treeZ, block.GLOWING_OBSIDIAN.id)

    # Add Sub-branches either side.
    for j in range(0, length, 3):
        length2 = int((length -j) *0.75)
        mc.setBlocks(treeX-j, i, treeZ, treeX-j, i, treeZ+length2, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX-j, i-1, treeZ+length2, block.WOOL.id, randint(1,14))
        mc.setBlocks(treeX-j, i, treeZ, treeX-j, i, treeZ-length2, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX-j, i-1, treeZ-length2, block.WOOL.id, randint(1,14))
        
    # Add the West facing branch.
    mc.setBlocks(treeX, i, treeZ, treeX, i, treeZ+length, block.LEAVES.id)

    # Add fairy lights to some branches.
    if (randint(0,1) == 1):
        mc.setBlock(treeX, i+1, treeZ+length, block.GLOWING_OBSIDIAN.id)

    # Add Sub-branches either side.
    for j in range(0, length, 3):
        length2 = int((length -j) *0.75)
        mc.setBlocks(treeX, i, treeZ+j, treeX+length2, i, treeZ+j, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX+length2, i-1, treeZ+j, block.WOOL.id, randint(1,14))
        mc.setBlocks(treeX, i, treeZ+j, treeX-length2, i, treeZ+j, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX-length2, i-1, treeZ+j, block.WOOL.id, randint(1,14))
        
    # Add the East facing branch.
    mc.setBlocks(treeX, i, treeZ, treeX, i, treeZ-length, block.LEAVES.id)

    # Add fairy lights to some branches.
    if (randint(0,1) == 1):
        mc.setBlock(treeX, i+1, treeZ-length, block.GLOWING_OBSIDIAN.id)

    # Add Sub-branches either side.
    for j in range(0, length, 3):
        length2 = int((length -j) *0.75)
        mc.setBlocks(treeX, i, treeZ-j, treeX+length2, i, treeZ-j, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX+length2, i-1, treeZ-j, block.WOOL.id, randint(1,14))
        mc.setBlocks(treeX, i, treeZ-j, treeX-length2, i, treeZ-j, block.LEAVES.id)
        if (randint(0,3) == 1):
            mc.setBlock(treeX-length2, i-1, treeZ-j, block.WOOL.id, randint(1,14))
 
raw_input("Press <Return> to restore the World.")
mc.restoreCheckpoint()
