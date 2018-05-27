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
p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)

# Wrap the main code in a try, except catcher
try:
    
    # Count from 50 to 90 in steps of 1
    for ii in range(50, 91): 


        # Divide by 10 to get 5.0 to 9.0 in steps of 0.1
        # Pass this value to the PWM and print the number to screen
        p.ChangeDutyCycle(ii / 10.0)
        print ii / 10.0

        # Wait for 1/2 second
        time.sleep(0.5)

# Catch if someone presses ctrl-C, stop looping       
except KeyboardInterrupt:
    pass

# Clean up PWM and GPIO
p.stop()
GPIO.cleanup()
