from gpiozero import Button

button=Button(4)

button.wait_for_release()
print ("Door opened")
