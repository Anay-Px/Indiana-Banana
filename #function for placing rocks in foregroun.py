     #function for placing rocks in foreground
rockdrawer = turtle.Turtle
def rock_setup(x2):
  rockdrawer = turtle.Turtle()
  rockdrawer.hideturtle()
  wn.tracer(False)
  rockdrawer.speed = 0
  rockdrawer.penup()
  rockdrawer.goto(x2,-295)
  rockdrawer.pendown()
  rockdrawer.fillcolor("grey")
  rockdrawer.begin_fill()
  rockdrawer.left(85)
  rockdrawer.forward(110)
  rockdrawer.right(170)
  rockdrawer.forward(110)
  rockdrawer.right(95)
  rockdrawer.forward(20)
  rockdrawer.end_fill()
  wn.tracer(True)