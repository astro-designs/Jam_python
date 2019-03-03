#!/usr/bin/python
from sense_hat import SenseHat
import sys

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

if len(sys.argv) > 1:
    for x in range (1, len(sys.argv)):
        sense.show_message(sys.argv[x])
else:
    sense.show_message("What shall we do today?", text_colour=blue)
