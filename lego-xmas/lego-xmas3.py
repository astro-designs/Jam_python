from gpiozero import PWMLED
from time import sleep

red=PWMLED(14)
blue=PWMLED(15)
yellow=PWMLED(18)

while True:
  red.pulse(0.3,0.3,4,True)
  blue.pulse(0.4,0.4,3,True)
  yellow.pulse(0.6,0.6,2,True)
  sleep(2.4)

# PWMLEDs have a pulse command. The parameters are:
# 1 Fade in time, in seconds
# 2 Fade out time, in seconds
# 3 Number of times to pulse
# 4 Background - True to continue to the next command without waiting
#                False to wait until finished
#
# For example:
# red.pulse(0.3,0.3,4,True)
# * Fade in for 0.3 seconds
# * Fade out for 0.3 seconds
# * Repeat 4 times
# * Continue with the next command without waiting
# 4x0.3=1.2 seconds to fade in
# 4x0.3=1.2 seconds to fade out
# 1.2+1.2=2.4 seconds total
#
# Find out more about PWMLED commands
# http://gpiozero.readthedocs.io/en/stable/api_output.html#pwmled
#
# Learn about PWM Pulse Width Modulation
# https://learn.sparkfun.com/tutorials/pulse-width-modulation
