import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Simple 2D Platformer")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.addshape("\\dohome2.pusd.dom\Home2$\Student2\1970688\code\player.gif")

# Create ground
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(-400, -240)
pen.fillcolor("sienna")
pen.begin_fill()
pen.setheading(0)
pen.forward(1000)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(1000)
pen.right(90)
pen.forward(200)
pen.end_fill()

# Player settings
player = turtle.Turtle()
player.shape("\\dohome2.pusd.dom\Home2$\Student2\1970688\code\player.gif")
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
    spike.shape("triangle")
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

    check_collision()  # Check for collisions with spikes
    check_goal()  # Check for goal every update
    wn.ontimer(update, 20)  # Call update every 20 ms



def level1():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1

def level2():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1

def level3():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1

def level4():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1

def level5():
     spike([(-200, -260), (0, -260), (200, -260)])  # Initial spikes for Level 1

def draw_level():
    global level_counter
    if level_counter == 1:
        print("Starting Level 1 Surface")
        level1()


    elif level_counter == 2:
        wn.bgcolor("lightgray")
        print("Starting Level 2 entrance of cave")
        level2()


    elif level_counter == 3:
        wn.bgcolor("gray")
        print("Starting Level 3 boulder chase")
        level3()

    elif level_counter == 4:
        wn.bgcolor("darkgray")
        print("Starting Level 4 trap")
        level4()

    elif level_counter == 5:
        wn.bgcolor("lightyellow")
        print("Starting Level 5 banana room")
        level5()
    else:
        print("All levels completed!")

def stop_movement():
    global horizontal_velocity
    horizontal_velocity = 0

# Function to move left
def move_left():
    global horizontal_velocity
    horizontal_velocity = -5  # Set velocity for moving left

# Function to move right
def move_right():
    global horizontal_velocity
    horizontal_velocity = 5  # Set velocity for moving right

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

# Main game loop
wn.mainloop()