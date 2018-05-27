import time
import RPi.GPIO as GPIO

##################################################################
# PWM is pulse width modulation: a pulse of variable width (0 - 100%)
# sent 50 time per second.
#
# PWM range for these servos is 5% to 9%.  
# 
# -  7% is stationaral. 
# -  < 7% rotates one way
# -  > 7% the other
#
##################################################################

# Set up GPIO to use numbers of the pins, not from the chip
GPIO.setmode(GPIO.BOARD)

# Set pins 12 as an output
GPIO.setup(12, GPIO.OUT)

# Start pin 12 as a 50Hz PWM pin and start it 
lw = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
lw.start(0)

# Set pins 16 as an output
GPIO.setup(16, GPIO.OUT)

# Start pin 16 as a 50Hz PWM pin and start it
rw = GPIO.PWM(16, 50)  # channel=16 frequency=50Hz
rw.start(0)

# Wrap the main code in a try, except catcher
try:
    ii = 50
    increment = 0

    while True:

        # The range of PWM is 5% to 9% of 50Hz.  Step through this range 
        # by ones
        if ii < 50:
            increment = 1 
        if ii > 90:
            increment = -1

        ii += increment

        # Divide the 50 - 90 range by 10 to get 5.0% to 9.0% in steps of 0.1%
        # Pass this value to the PWM and print the number to screen.
        # The left wheel (lw) and right wheel (rw) spin in opposite directions
        lw.ChangeDutyCycle(ii / 10.0)
        rw.ChangeDutyCycle((140 - ii) / 10.0)
        print ii / 10.0

        # Wait for 0.1 second
        time.sleep(0.1)

# Catch if someone presses ctrl-C and stop looping       
except KeyboardInterrupt:
    pass

# Clean up PWM and GPIO
lw.stop()
rw.stop()
GPIO.cleanup()
