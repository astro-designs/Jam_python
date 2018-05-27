from gpiozero import LED
from time import sleep

red=LED(14)
blue=LED(15)
yellow=LED(18)

while True:
  blue.off()
  yellow.off()
  red.on()
  sleep(0.5)

  red.off()
  blue.on()
  sleep(0.5)

  blue.off()
  yellow.on()
  sleep(0.5)
