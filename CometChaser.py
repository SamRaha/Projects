""" Python Turtle Graphics Game Using Classes by Sam Raha
1) set up screen
2) keyboard bindings
3) add a border / border checking
4) adding a goal / Moving the goal around
5) collision checking
6) multiple goals and improve performance
7) implement a scoring system
8) background Image (ms paint)/ Sound (winsound)
9) changge the turtle image (balls to comets)
10) create enemies (these would be planets that you would want to avoid. will make you lose score (same as the balls but give you negative points with different colour)
"""


import turtle
import random
import math
import winsound

# set up screen

wn = turtle.Screen()  # turtle screen object
wn.bgcolor("black")  # bgcolour is a method that changes the backgroun colour to red
wn.title("Simple Python Turtle Graphics Game (Class Version)")
wn.bgpic("bkground1.gif")  # background picture that is in the same folder as the python game
# wn.register_shape("broccoli.gif")  # built in method.. this changes the balls


class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 300)
        self.score = 0

    def update_score(self):
        self.clear()  # clear current score
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))  # write the new score with the formatting

    def change_score(self, points):
        self.score += points  # 1 point coming from instance
        self.update_score()  # once do, update tthe score

    def play_sound(self):
        winsound.PlaySound('photon.wav', winsound.SND_ASYNC)  # async makes sure the sound plays in the background

# border class below. border is a child of the turtle.Turtle class


class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()  # we dont want to draw soemthing
        self.hideturtle()  # don't need to see  it
        self.speed(0)  # speed is a method here, it's the animation speed. do not animate, draw as fast as you can. different to the Player speed
        self.color("white")  # border to be white
        self.pensize(5)  # size is 5 pixels

    def draw_border(self):
        self.penup()  # pen up then takes you to the below coordinates
        self.goto(-300, -300)  # left bottom corner
        self.pendown()  # it means you can start drawing
        self.goto(-300, 300)  # left up xxyy
        self.goto(300, 300)  # right up
        self.goto(300, -300)  # right down
        self.goto(-300, -300)  # left down

 # creating your player using classes


class Player(turtle.Turtle):  # player is a sub class of turtle class. everything the turtle can do, the player can now do.

    def __init__(self):  # initialise purple
        turtle.Turtle.__init__(self)  # init player
        self.penup()  # part of the turtle class
        self.speed(0)  # draws it without any time. so the player moves fast as possible
        self.shape("triangle")  # part of the turtle class
        self.color("white")  # part of the turtle class
        self.speed = 1  # not part of the turtle class

    # jump makes the self go to a random location

    def move(self):
        self.forward(self.speed)  # moves turtle forward on the screen at the speed of the current turtle which is 1

        # border checking: if the player(self) gets to to the right and left far side. it turns left
        if self.xcor() > 280 or self.xcor() < -280:
            self.left(60)
        if self.ycor() > 280 or self.ycor() < -280:
            self.left(60)

    # the below code define rules that are linked to the keyboard bindings

    def turnleft(self):
        self.left(30)  # 30 degrees

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def decreasespeed(self):
        self.speed -= 1


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)  # animation is 0
        self.color("red")
        self.shape("circle")
        self.speed = 1  # moves fast
        self.goto(random.randint(-250, 250), random.randint(-250, 250))  # starts at random location. the first random is thr xcor and the second is ycor
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # border checking
        if self.xcor() > 280 or self.xcor() < -280:
            self.left(45)
        if self.ycor() > 280 or self.ycor() < -280:
            self.left(45)
    # Collision checking function
    # Uses the Pythagorean Theorem to measure the distance beween two objects


def isCollision(t1, t2):  # "is" return true or flase
    a = t1.xcor() - t2.xcor()  # calcualte difference between the x coordinates
    b = t1.ycor() - t2.ycor()  # and y
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False


# create class instances
player = Player()  # this is a class instance. it's the player object. self is player.
border = Border()
game = Game()  # updates the score

# draw border onces
border.draw_border()

# create multiple goals
goals = []
for count in range(6):
    goals.append(Goal())  # new turtle called goal that has all attributes of goal class


# set keyboard bindings
turtle.listen()  # the turtle module has listen, this listens for keyboard presses
turtle.onkey(player.turnleft, "Left")  # onkey is a method , when you press left key, it reads from the def turnleft, which turns the player left
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")
turtle.onkey(player.decreasespeed, "Down")

# Speed up the game using a tracer
wn.tracer(0)  # stops the screen from being updated


# Main Loop

while True:  # repeats until break
    wn.update()  # we update the screen in the loop only in the memory and then updates the screen. only update each time through rather than each step of the way
    player.move()  # make our player(insance/object) move(function)
    for goal in goals:
        goal.move()

        # checks for a collision between player and goal
        if isCollision(player, goal):
            goal.jump()
            game.change_score(1)  # jump from the functions
            game.play_sound() #plays sound from the function
