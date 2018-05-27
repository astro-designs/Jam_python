from gpiozero import Button

button=Button(4)

while (True):
  button.wait_for_release()
  print ("Door opened")

  button.wait_for_press()
  print ("Door closed")
