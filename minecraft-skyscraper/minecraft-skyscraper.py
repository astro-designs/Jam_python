#!/usr/bin/env python
#########################################################
#
# Build a flight of steps in Minecraft.
#
#########################################################
from mcpi import minecraft
from mcpi import block

# How many stairs to be made.
size = 8
levels = 8
level = 0

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Find out where the Player is (we want to build near here)
x, y, z = mc.player.getTilePos()
print "Making the Skyscraper at: " + str(x + 2) + ", " + str(z)

# Build the base
mc.setBlocks(x+1, y-1, z-size/2, x+size+3, y-1, z+size/2, block.STONE)

# Build a series of levels.
#for level in range(levels):

# Build a series of staggered bricks.
for step in range(size):
    mc.setBlock(x+step+2, level*size+y+step, z, block.STAIRS_WOOD.id, 0)
    mc.setBlock(x+step+3, level*size+y+step, z, block.WOOD.id)

# Build the ceiling
#mc.setBlocks(x+1, y+size+level*size-1, z-size/2, x+size+3, y+size+level*size-1, z+size/2, block.STONE)
#mc.setBlocks(x+2+size/2, y+size+level*size-1, z, x+size+2, y+size+level*size-1, z, block.AIR)

# Build glass walls
#mc.setBlocks(x+1, y+level*size, z-size/2, x+1, y+level*size+size, z+size/2, block.GLASS_PANE)
#mc.setBlocks(x+size+3, y+level*size, z-size/2, x+size+3, y+level*size+size, z+size/2, block.GLASS_PANE)
#mc.setBlocks(x+1, y+level*size, z-size/2, x+size+3, y+level*size+size, z-size/2, block.GLASS_PANE)
#mc.setBlocks(x+1, y+level*size, z+size/2, x+size+3, y+level*size+size, z+size/2, block.GLASS_PANE)

###########################
# Exercises:
#    Write or edit the code to do the following:
#    Easy:
#        Change the Materials used.
#        Change the number of floors or height of each floor.
#    Medium:
#        Change the Width of the steps.
#        Add entrance door(s).
#    Advanced:
#        Place a helicopter pad on the top of the Skysraper.
#        Make changes to the design of the Skyscraper.


