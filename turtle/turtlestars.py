from turtle import *

color("WhiteSmoke")
bgcolor("MidnightBlue")
pendown()
begin_fill()

#draw the star shape
for side in range(5):
  left(144)
  forward(50)

end_fill()
penup()

forward(100)
done()
