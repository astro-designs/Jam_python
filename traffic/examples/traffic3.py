import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red=11
yellow=13
green=15

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

while (True):

  GPIO.output(yellow, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(yellow, GPIO.LOW)
  time.sleep(2)
