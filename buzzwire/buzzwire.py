from time import sleep
from os import system
from gpiozero import Button, LED

led = LED(4)
button = Button(26)

while True:
    if button.is_pressed:
        print("BUZZZZZZ")
        led.on()
        system("aplay buzzer.wav &")
        sleep(1)
        led.off()
