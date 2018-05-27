from gpiozero import Button, Buzzer

button=Button(4)
buzzer=Buzzer(23)

while (True):
  button.wait_for_release()
  print ("Door opened")
  buzzer.beep(1,0,1)

  button.wait_for_press()
  print ("Door closed")
