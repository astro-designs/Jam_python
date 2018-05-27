from gpiozero import LED

led=LED(4)

# Blink the time signal
# 6 short flashes followed by 1 long
led.blink(0.5,0.5,6,False)
led.blink(1,0,1,False)

# led.blink() has 4 parameters:
#   On time, in seconds, can be decimal fraction
#   Off time, in seconds, can be decimal fraction
#   Repeats, a whole number
#     or the value None which means forever
#     default is None
#   Background, whether to wait (False)
#     or carry on (True) (default is True)
# Try to blink SOS in Morse Code
# S = short short short
# O = long long long
