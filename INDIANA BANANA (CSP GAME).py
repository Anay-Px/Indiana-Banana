import turtle


# Set up the screen
wn = turtle.Screen()
wn.title("Indiana Banna")
wn.bgpic("Level1.png")
wn.setup(width=800, height=600)
wn.addshape("player.gif")
wn.addshape("player_standing.gif")
wn.addshape("player_backward.gif")


wn.addshape("spike.gif")
wn.addshape("rolling_spike.gif")
#wn.addshape("goal.gif")


# Player settings
screen= turtle.Screen()
enemy= turtle.Turtle()
player = turtle.Turtle()
player.shape("player_standing.gif")
enemy.shape("rolling_spike.gif")

player.penup()
player.speed(0)
player.goto(-350, -220)


# Level variables
spikes = []  # List to hold spikes
level_counter = 1
gravity = -0.5
jump_height = 10
is_jumping = False
vertical_velocity = 0
horizontal_velocity = 0


def create_spike(x, y):
    spike = turtle.Turtle()
    spike.speed(0)
    spike.setheading(90)
    spike.shape("spike.gif")
    spike.color("red")
    spike.penup()
    spike.goto(x, y)
    spikes.append(spike)  # Add the new spike to the list


def spike(positions):
    for x, y in positions:
        create_spike(x, y)  # Create each spike at the specified position


# Function to handle jumping
def jump():
    global is_jumping, vertical_velocity
    if not is_jumping:
        is_jumping = True
        vertical_velocity = jump_height


def reset_level():
    print("Collision detected! Resetting level...")
    player.goto(-350, -220)  # Reset player position


def check_collision():
    for spike in spikes:
        if player.distance(spike) < 48:  # Check for collision with any spike
            reset_level()
def check_collision2():
    if player.distance(enemy) < 60:  # Check for collision with any spike
        reset_level()


def check_goal():
    global level_counter
    if player.xcor() > 385:  # Check if player walks off the right side
        level_counter += 1
        draw_level()
        player.goto(-350, -220)  # Reset player position to start of level
    if player.xcor() < -385:  # Check if player walks off the left side
        playery = player.ycor()
        player.goto(-384, playery)


# Function to update player position
def update():
    global is_jumping, vertical_velocity, horizontal_velocity


    # Update horizontal position
    player.setx(player.xcor() + horizontal_velocity)


    if is_jumping:
        player.sety(player.ycor() + vertical_velocity)
        vertical_velocity += gravity
        if player.ycor() <= -220:  # Ground level
            player.sety(-220)
            is_jumping = False
            vertical_velocity = 0  # Reset vertical velocity upon landing
    check_collision2()
    check_collision()  # Check for collisions with spikes
    check_goal()  # Check for goal every update
    wn.ontimer(update, 1)  # Call update every 20 ms
 # Call update every 20 ms


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
enemy.pu()
enemy.goto(500,-250)
direction = 15


def move_enemy():
    global direction
    enemy.forward(direction) # Move up
    if (enemy.xcor() > 300 ):  # Check top boundary
        direction= -20
    elif(enemy.xcor() <-300):
        direction= 20  # Reset position
    screen.ontimer(move_enemy, 20)  # Repeat
enemy.hideturtle()
def level1():
     
     spike([(-200, -260), (-175, -260), (-150, -260), (-70, -130), (-45, -130), (100,-260),(100, -240)])  # Initial spikes for Level 1
     
def level2():
 
  spike([(-200, -260), (-200, -240), (-200, -220), (-290, -160), (0, -260), (25, -260),(50,-260),(75, -200), (180,-260) ])  # Initial spikes for Level 1


def level3():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1


def level4():
     spike([(-100, -260), (-75, -260), (-50, -260), (-25,-260), (0,-260), (-200, -260), (-200, -240), (-200, -220), (-200, -200), (-150, -80), (85, -260), (85, -240), (85, -220), (95, -200), (105, -180),(220,-190), (220, -60), (240, -180), (240, -55), (260, -190),(260, -60)])  # Initial spikes for Level 1

def level5():
    enemy.goto(0, -250)
    spike([(-200, -260), (-200, -240), (-200, -220), (-70, -260), (0, -260),(90,-260),(75, -200), (200,-260) ])
    enemy.showturtle()

    move_enemy()

def level6():
     enemy.hideturtle
     clear_spikes()
     wn.bgpic("Level5.png")
     goal = turtle.Turtle()
     goal.shape("goal.gif")
     goal.penup()
     goal.speed(0)
     goal.goto(350, -220)


     if player.distance(goal) < 48:  # Check for collision with any spike
        reset_level()



def level7():
    endwriter = turtle.Turtle()
    endwriter.hideturtle()
    endwriter.speed(0)
    endwriter.setheading(90)
    endwriter.penup()
    endwriter.setposition(-270,50)
    endwriter.pendown()
    endwriter.write("Thanks for Playing",  font = ("Arial", 50, "normal"))
    wn.bgcolor("gray")
    player.hideturtle()






def clear_spikes():
    for spike in spikes:
        spike.hideturtle()  # Hide the spike
    spikes.clear()  # Clear the list of spikes


def draw_level():
    global level_counter
    clear_spikes()  # Clear existing spikes before starting a new level
   
    if level_counter == 1:
        print("Starting Level 1")
        level1()


    elif level_counter == 2:
        wn.bgpic("level2.png")
        print("Starting Level 2")
        level2()


    elif level_counter == 3:
        wn.bgpic("level3.png")
        print("Starting Level 3")
        level3()


    elif level_counter == 4:
        wn.bgpic("level4.png")
        print("Starting Level 4")
        level4()


    elif level_counter == 5:
        wn.bgpic("level5.png")
        print("Starting Level 5")
        level5()
       
    elif level_counter == 6:
        wn.bgcolor("red")

        level6()
    elif level_counter == 7:
        wn.bgcolor("lightyellow")
        print("Game Over, Thanks for Playing")
        level7()


    else:
        print("All levels completed!")


def stop_movement():
    global horizontal_velocity
    horizontal_velocity = 0
    if horizontal_velocity == 0:
        player.shape("player_standing.gif")
    elif horizontal_velocity>0:
        player.shape("player.gif")
    else:
        player.shape("player_backward.gif")


# Function to move left
def move_left():
    global horizontal_velocity
    horizontal_velocity = -5  # Set velocity for moving left
    if horizontal_velocity == 0:
        player.shape("player_standing.gif")
    elif horizontal_velocity>0:
        player.shape("player.gif")
    else:
        player.shape("player_backward.gif")


# Function to move right
def move_right():
    global horizontal_velocity
    horizontal_velocity = 5
    if horizontal_velocity == 0:
        player.shape("player_standing.gif")
    elif horizontal_velocity>0:
        player.shape("player.gif")
    else:
        player.shape("player_backward.gif")


# Start the level
draw_level()  # Call this to initialize spikes for Level 1


# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeyrelease(stop_movement, "a")  # Stop moving left
wn.onkeyrelease(stop_movement, "d")  # Stop moving right
wn.onkeypress(jump, "w")


# Start the update loop
update()
turtle.done()


# Main game loop
wn.mainloop()