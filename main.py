#   a123_apple_1.py
import turtle as trtl
import random


#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
###############################

apple = trtl.Turtle()
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()

#############################
letters = ["a","b","c","d","e","f","g","h"]


xcor= random.randint(-150,150)
ycor= random.randint(-40,100)
#-----functions-----
appleLetters="a"
active_apple = apple 

# given a turtle, set that turtle to be shaped by the image file


turtle_list = [apple, apple1, apple3, apple4]


def draw_apple(active_apple):
  for i in range turtle_list:
    
    apple.pu()
    global appleLetters
    appleLetters= letters[random.randint(0,7)]
    active_apple.shape(apple_image)
    wn.tracer(False)
    active_apple.setx(random.randint(-175,175))
    active_apple.sety(random.randint(-25,100))
    active_apple.sety(active_apple.ycor()-35)
    active_apple.write(appleLetters, align = 'center', font=("Arial", 30, "bold"))
    active_apple.sety(active_apple.ycor()+35)


  wn.tracer(True)
  wn.update()


def drop_apple():
  apple.pu()
  apple.clear()
  apple.sety(-150)
  draw_apple(apple)






#-----function calls-----

draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.onkeypress(drop_apple, "b")
wn.onkeypress(drop_apple, "c")
wn.onkeypress(drop_apple, "d")
wn.onkeypress(drop_apple, "e")
wn.onkeypress(drop_apple, "f")
wn.onkeypress(drop_apple, "g")
wn.onkeypress(drop_apple, "h")

wn.listen()
wn.mainloop()