from time import sleep
from os import system
from gpiozero import Button

button = Button(4)
print ("Don't hurt me!")
while True:
  button.wait_for_press()
  print ("Ouch!")
  system("omxplayer scream-c.wav")
        
