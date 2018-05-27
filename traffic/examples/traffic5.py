#!/usr/bin/env python
# GPIO traffic lights by Andrew Oakley for Cotswold Raspberry Jam
# http://www.cotswoldjam.org September 2015 Public Domain

# Start by reading the library about GPIO pins and timing
import RPi.GPIO as GPIO, time, signal, sys

# Set up the GPIO pins
# We're using board numbering as it works for all Pis
# including original Rev.1 boards
GPIO.setmode(GPIO.BOARD)

# Turn off warnings, notably if the pins are already set
GPIO.setwarnings(False)

# Turn off lights if process is killed
def signal_term_handler(signal, frame):
  GPIO.output(red, GPIO.LOW)
  GPIO.output(yellow, GPIO.LOW)
  GPIO.output(green, GPIO.LOW)
  print 'got SIGTERM'
  sys.exit(0)
signal.signal(signal.SIGTERM, signal_term_handler)

# Which colours are on which pins?
# You can use pin 9 for ground
# Attach ground to the shortest leg of the LED
red=11
yellow=13
green=15

# Set up the pins for output
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# We use TRY and EXCEPT to allow us to
# turn the lights off after stopping the
# program using CTRL-C, or during shutdown
try:

  # Loop round forever, until stopped by CTRL-C
  while (True):

    # Start with Red
    GPIO.output(red, GPIO.HIGH)
    time.sleep(5)

    # Leave red on, and turn yellow on too
    # Red & yellow together is mostly a British thing
    # Countries like France and the USA don't have it
    # they go straight from red to green
    GPIO.output(yellow, GPIO.HIGH)
    time.sleep(2)

    # Turn off red and yellow
    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)
    # Turn on green
    GPIO.output(green, GPIO.HIGH)
    time.sleep(5)

    # Turn off green
    GPIO.output(green, GPIO.LOW)
    # Turn on yellow
    GPIO.output(yellow, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(yellow, GPIO.LOW)

# If we have pressed CTRL-C, or if the computer
# is being shut down, then turn all lights off
except (KeyboardInterrupt, SystemExit):
  GPIO.output(red, GPIO.LOW)
  GPIO.output(yellow, GPIO.LOW)
  GPIO.output(green, GPIO.LOW)
  # Report the reason for stopping
  raise

# Now have a think about how you might expand this program
# A T-junction needs 3 sets of lights
# A crossroads needs 4 sets
# Could you wire all sets of lights from one Raspberry Pi?
# What about a left turn filter?
# At night some part-time lights just flash yellow
# If you had two Raspberry Pis, how could they communicate
# so that they could synchronise their lights?

