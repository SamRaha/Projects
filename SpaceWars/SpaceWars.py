

import random
import winsound
import turtle
import time


turtle.speed(0)  # controls the speed of animations. just draw ASAP.

turtle.ht()  # hides the default turtle
turtle.setundobuffer(1)  # stops using too much memory
turtle.tracer(0)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SPACEWARS)")
wn.bgpic("bkground1.gif")  # will change later. how oftne you want to update the screen

# sprite is a child class of turtle

# parent class


class Sprite(turtle.Turtle):  # sprites are characters on the screen
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)  # speed of animation 0 is fastest
        self.penup()  # no drawing yet
        self.color(color)  # define later
        self.goto(startx, starty)  # define later
        self.speed = 1  # movement speed

    def move(self):
        self.fd(self.speed)  # fd is forward

        # boundary detection
        if self.xcor() > 290:
            self.setx(290)  # if the sprite moves past x290, then it is set back at x290
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
# if players x cor was inside enemies area.

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):  # child class, grandchild of turtleclass
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)  # everything that is true in sprite will not initirlise itself in Player
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3  # players have lives, other sprites dont
        # you don't need the move function as it already exists for Sprite class.

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


# creating enemy
class Enemy(Sprite):  # child class, grandchild of turtleclass
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 5
        self.setheading(random.randint(0, 360))  # it will set its direction in a random direction of 0 to 360


class Ally(Sprite):  # child class, grandchild of turtleclass
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)  # fd is forward

        # boundary detection
        if self.xcor() > 290:
            self.setx(290)  # if the sprite moves past x290, then it is set back at x290
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)  # moves it to off the screen to begin with

    def fire(self):
        if self.status == "ready":
            winsound.PlaySound('photon.wav', winsound.SND_ASYNC)
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            # game.play_photon_sound()

    def move(self):
        if self.status == "firing":
            self.fd(self.speed)

        if self.status == "ready":
            self.goto(-1000, 1000)

        # border check
        if self.xcor() < -295 or self.xcor() > 295 or self.ycor() < - 295 or self.ycor() > 295:
            self.goto(-1000, 1000)
            self.status = "ready"


class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"  # whats the state, playing, not playing?
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)  # the pen is the turtle
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()  # hides turtle
        self.pen.pendown()

    # def play_crash_sound(self):
    #     winsound.PlaySound('crash.wav', winsound.SND_ASYNC)

    # def play_crash2_sound(self):
    #     winsound.PlaySound('crash2.wav', winsound.SND_ASYNC)

    # def play_music_sound(self):
    #     winsound.PlaySound('scifi.wav', winsound.SND_ASYNC)

    def show_status(self):
        self.pen.undo()  # this is where you undo the pendown, so it puts the pen back up from line 160 self.pen.pendown()
        msg = "Score: {}".format(self.score)
        self.pen.penup()
        self.pen.goto(-290, 300)
        self.pen.write(msg, font=("Arial", 16, "normal"))


class Particle(Sprite):  # child class, grandchild of turtleclass
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.goto(-1000, -1000)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.frame = 0  # starts on fame 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, 1000)


        # create my sprites
player = Player("triangle", "white", 0, 0)

# cclasses define what something is like... only when you create the instance you create it.
# create game object
game = Game()

# draw the game border
game.draw_border()


# show game status
game.show_status()
# enemy instance

# enemy = Enemy("circle", "red", 0, 0)
enemies = []
for i in range(3):
    enemies.append(Enemy("circle", "red", 100, 0))

# ally = Ally("turtle", "green", 0, 0)
allies = []
for i in range(3):
    allies.append(Ally("turtle", "green", -100, 0))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# for count in range(3):
# enemy.append(Enemy("circle", "red", 0, 0))

# create missile
missile = Missile("triangle", "yellow", 0, 0)

# keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()  # turtle to acklowendge


# Main Game Loop
while True:
    turtle.update()  # this only starts the tracer when the loop starts
    time.sleep(0.02)  # sleeps so it makes it go a little slower
    player.move()
    missile.move()

    for enemy in enemies:
        enemy.move()

    # check for a collision between player and enemy
        if player.is_collision(enemy):
            winsound.PlaySound('crash2.wav', winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()

    # check for a collission between missile and enemy
        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # increase the score
            game.score += 100
            game.show_status()
            # do the explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
    for ally in allies:
        ally.move()

    # check if collision between player and ally
        # if player.is_collision(ally):
        #     winsound.PlaySound('crash2.wav', winsound.SND_ASYNC)
        #     x = random.randint(-250, 250)
        #     y = random.randint(-250, 250)
        #     ally.goto(x, y)
        #     missile.status = "ready"
        #     game.score -= 50
        #     game.show_status()

        # check for a collission between missile and ally
        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            game.score -= 50
            game.show_status()

    for particle in particles:
        particle.move()

delay = input("Press enter to finish. > ")
