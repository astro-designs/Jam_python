#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red=11
yellow=13
green=15

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.output(red, GPIO.LOW)
GPIO.output(yellow, GPIO.LOW)
GPIO.output(green, GPIO.LOW)

