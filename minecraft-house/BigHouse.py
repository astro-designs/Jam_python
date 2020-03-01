#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

# Number of rooms...
xrooms = 1   # Change this constant to adjust the number of rooms in the x-axis (left-right)
zrooms = 1   # Change this constant to adjust the number of rooms in the z-axis (front-back)
floors = 1   # Change this constant to set the number of floors

# Room size...
width = 6    # Change this constant to set the width of each room
depth = 7    # Change this constant to set the depth of the room
height = 3   # Change this constant to set the height of each floor

for floor in range(floors):

    # Set the floor.
    if floor == 0:
        mc.setBlocks(x-1, y-1, z+2, x+(xrooms*width)+1, y-1, z+4+(zrooms*depth), block.COBBLESTONE.id)
    else:
        # Floor...
        mc.setBlocks(x, y-1, z+3, x+(xrooms*width), y-1, z+3+(zrooms*depth), block.COBBLESTONE.id)
        # Stair-well if more than one floor
        if floors > floor:
            # Clear a stair-well to the next level...
            mc.setBlocks(x+2, y-1, z+5, x+3, y-1, z+5+height-1, block.AIR.id)
            # Place the final step
            mc.setBlocks(x+2, y-1, z+5+height, x+3, y-1, z+5+height, block.STAIRS_WOOD.id, 2)
                
    for zroom in range(zrooms):
        for xroom in range(xrooms):
            # Create a hollow shell made of bricks.
            mc.setBlocks(x+(xroom*width), y, z+(zroom*depth)+3, x+(xroom*width)+width, y+height, z+3+(zroom*depth)+depth, block.BRICK_BLOCK.id)
            mc.setBlocks(x+(xroom*width)+1, y, z+(zroom*depth)+4, x+(xroom*width)+width-1, y+height-1, z+2+(zroom*depth)+depth, block.AIR.id)

            # Add Windows.
            mc.setBlocks(x+(xroom*width)+3, y+1, z+(zroom*depth)+3, x+(xroom*width)+4, y+2, z+(zroom*depth)+3, block.GLASS.id)
            mc.setBlocks(x+(xroom*width)+2, y+1, z+(zroom*depth)+3+depth, x+(xroom*width)+3, y+2, z+(zroom*depth)+3+depth, block.GLASS.id)
            mc.setBlocks(x+(xroom*width), y+1, z+(zroom*depth)+6, x+(xroom*width), y+2, z+(zroom*depth)+7, block.GLASS.id)
            mc.setBlocks(x+(xroom*width)+width, y+1, z+(zroom*depth)+5, x+(xroom*width)+width, y+2, z+(zroom*depth)+7, block.GLASS.id)

            if floor == 0 and xroom == 0 and zroom == 0:
                # Add a front door.
                mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
                mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

            if zroom > 0:
                # Add a Door to connect rooms down the z-axis.
                mc.setBlock(x+(xroom*width)+1, y, z+(zroom*depth)+3, block.DOOR_WOOD.id, 0)
                mc.setBlock(x+(xroom*width)+1, y+1, z+(zroom*depth)+3, block.DOOR_WOOD.id, 8)

            if zroom == 0 and xroom > 0:
                # Add a Door to connect rooms along the x-axis.
                mc.setBlock(x+(xroom*width), y, z+(zroom*depth)+4, block.DOOR_WOOD.id, 0)
                mc.setBlock(x+(xroom*width), y+1, z+(zroom*depth)+4, block.DOOR_WOOD.id, 8)

            if floors > 0 and xroom == 0 and zroom == 0 and floors > floor:
                # Add some stairs to the next level...
                for i in range(height):
                    mc.setBlocks(x+2, y+i, z+5+i, x+3, y+i, z+5+i, block.STAIRS_WOOD.id, 2)

    # Set the y coordinate to the next floor level, if there is another floor
    if floor < floors-1:
        y = y + (height+1)

# Add a Roof.

roof_width = width * xrooms
roof_depth = depth * zrooms

for i in range(roof_width//2 + 1):
    mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+roof_depth, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+roof_width-i, y+height+i, z+3, x+roof_width-i, y+height+i, z+3+roof_depth, block.STAIRS_WOOD.id, 1)
    # Gable ends.
    if ((roof_width//2) - i > 0):
        mc.setBlocks(x+1+i, y+height+i, z+3, x+roof_width-i-1, y+height+i, z+3, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+height+i, z+3+roof_depth, x+roof_width-i-1, y+height+i, z+3+roof_depth, block.BRICK_BLOCK.id, 1)
        
