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
    left = 70
    right = 70

    while True:

        command = raw_input("?")
        if command == "":
            left = 70
            right = 70
        elif command == "W" or command == "w":
            left = 80
            right = 60
        elif command == "A" or command == "a":
            left = 80
            right = 80
        elif command == "S" or command == "s":
            left = 60
            right = 80
        elif command == "D" or command == "d":
            left = 60
            right = 60
        else:
            left = 70
            right = 70

        # Divide by 10 to get 5.0 to 9.0 in steps of 0.1
        # Pass this value to the PWM and print the number to screen
        lw.ChangeDutyCycle(left / 10.0)
        rw.ChangeDutyCycle(right / 10.0)

# Catch if someone presses ctrl-C, stop looping       
except KeyboardInterrupt:
    pass

# Clean up PWM and GPIO
lw.stop()
rw.stop()
GPIO.cleanup()
