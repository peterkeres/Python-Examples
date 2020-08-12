"""
peter keres
10 25 2017

using loops to make a cave that holds an evil wizard!!!
"""

import random

# getting turle set up
import turtle

turtle.mode('logo')
turtle.speed(0)
turtle.shape('turtle')

colorlist = ["blue", "green", "purple", "hotpink", "salmon"]


def makecloud():
    turtle.pencolor("lightgray")
    turtle.begin_fill()
    turtle.fillcolor("lightgray")
    turtle.circle(10)
    turtle.end_fill()


def makecloudwhole():
    for cloud in range(0, 5, 1):
        makecloud()
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        makecloud()
    turtle.right(180)
    turtle.forward(10)
    turtle.left(180)
    makecloud()
    for cloud in range(0, 5, 1):
        makecloud()
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        makecloud()
    turtle.forward(10)
    makecloud()


def squareblock(size):
    turtle.pendown()
    turtle.pencolor("slategray")
    turtle.fillcolor("slategray")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    turtle.penup()


def maketreeleaf():
    turtle.pendown()
    turtle.pencolor("green")
    turtle.begin_fill()
    turtle.fillcolor("green")
    turtle.circle(2)
    turtle.end_fill()
    turtle.penup()


def maketree(trunk, size):
    """ this makes a tree """
    turtle.setheading(0)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor("brown4")
    turtle.fillcolor("brown4")
    turtle.begin_fill()
    turtle.forward((trunk * .5))  # send full base len and this will take for each side
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(trunk)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward((trunk * .5))
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(12)
    turtle.right(90)
    for leaf in range(0, 8, 1):  # row one
        maketreeleaf()
        turtle.right(90)
        turtle.forward(4)  # take size of circle and double it
        turtle.left(90)
    turtle.setheading(0)
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)
    for leaf in range(0, 6, 1):  # row two
        maketreeleaf()
        turtle.left(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.setheading(0)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(16)
    turtle.right(90)
    for leaf in range(0, 4, 1):  # row three
        maketreeleaf()
        turtle.right(90)
        turtle.forward(4)
        turtle.left(90)
    turtle.setheading(0)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(16)
    turtle.left(90)
    for leaf in range(0, 2, 1):  # row four
        maketreeleaf()
        turtle.left(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.setheading(0)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(6)
    turtle.left(90)
    maketreeleaf()  # top row


def arm(lenth, color, color2):  # FIXME:try to fix this so it goes out from the center
    angle1 = random.randint(-90, 90)
    angle2 = random.randint(-90, 90)
    angle3 = random.randint(-90, 90)
    angle4 = random.randint(-90, 90)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.forward(lenth)
    turtle.right(angle1)
    turtle.forward(lenth)
    if angle1 > 0:
        turtle.left(angle2)
    else:
        turtle.right(angle2)
    turtle.forward(lenth)
    if angle2 < 0:
        turtle.left(angle3)
    else:
        turtle.right(angle3)
    turtle.forward(lenth)
    if angle3 > 0:
        turtle.left(angle4)
    else:
        turtle.right(angle4)
    turtle.forward(lenth)
    turtle.begin_fill()
    turtle.fillcolor(color2)
    turtle.circle(2.5)
    turtle.end_fill()
    turtle.penup()


def makeflower(stemside, stemtop, inner, outter, color, st1, st2):
    """ lenth of the stem / width of stem / the size of inner circle / size of outter circles /
    the color of the outter circles / the x of the of the inner circle / y of the inner circle
    """
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(inner)
    turtle.end_fill()
    turtle.goto(st1, st2)  # for the stem
    turtle.setheading(0)
    turtle.circle(inner, 270)
    turtle.setheading(0)
    turtle.pendown()
    turtle.right(90)
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward((stemtop * .5))
    turtle.right(90)
    turtle.forward(stemside)
    turtle.right(90)
    turtle.forward(stemtop)
    turtle.right(90)
    turtle.forward(stemside)
    turtle.right(90)
    turtle.forward((stemtop * .5))
    turtle.end_fill()
    turtle.penup()
    for petal in range(0, 360, 40):
        turtle.goto(st1, st2)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(inner, petal)
        turtle.setheading((-petal + 180))
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(outter)
        turtle.end_fill()
        turtle.penup()


# making the sky?
turtle.penup()
turtle.left(90)
turtle.forward(650)  # each side from center is 650
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.right(90)
turtle.forward(360)  # top and bot is 360 from center
turtle.right(90)
turtle.forward(1300)
turtle.right(90)
turtle.forward(360)
turtle.right(90)
turtle.forward(1300)
turtle.right(90)
turtle.end_fill()
turtle.penup()

# getting the stars in the sky
turtle.shape("classic")
turtle.color("snow")
numstar = random.randint(8, 16)
# for right half of screen
for i in range(0, numstar, 1):
    randx = random.randint(0, 650)
    while 450 <= randx <= 575:  # so the starts dont end up on the moon and look wack
        randx = random.randint(0, 650)
    randy = random.randint(100, 380)
    while 225 <= randy <= 325:
        randy = random.randint(100, 380)
    turtle.goto(randx, randy)
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.stamp()
    turtle.setheading(0)
    # for left half of screen
for i in range(0, numstar, 1):
    randx = random.randint(-650, 0)
    randy = random.randint(100, 380)
    turtle.goto(randx, randy)
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.stamp()
    turtle.setheading(0)

# making the mountian
turtle.home()
turtle.pendown()
turtle.pencolor("gray")
turtle.begin_fill()
turtle.fillcolor("gray")
turtle.left(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(135)
turtle.forward(100)
turtle.end_fill()
turtle.penup()
# the whole inside the mountian
turtle.home()
turtle.right(90)
turtle.forward(90)  # O.G was 80
turtle.left(90)
turtle.pendown()
turtle.pencolor("black")
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(50, 180)  # O.G. was 40,180
turtle.end_fill()
turtle.right(180)
turtle.penup()

# making the elements in the sky
# making the moon
turtle.home()
turtle.color("yellow")
turtle.goto(500, 285)
turtle.pendown()
turtle.pencolor("lightgoldenrod")
turtle.begin_fill()
turtle.fillcolor("lightgoldenrod")
turtle.circle(50)
turtle.end_fill()
turtle.penup()
# the cut out for the moon
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.pencolor("black")
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(50)
turtle.end_fill()
turtle.penup()

# making clouds
# cloud 1
turtle.goto(-450, 255)
makecloudwhole()
# cloud 2
turtle.goto(-65, 310)
makecloudwhole()
# cloud 3
turtle.goto(150, 185)
makecloudwhole()
# cloud 4
turtle.goto(285, 285)
makecloudwhole()

# making the ground
# ground base
turtle.goto(0, 0)
turtle.penup()
turtle.right(90)
turtle.forward(650)
turtle.pendown()
turtle.pencolor("saddlebrown")
turtle.begin_fill()
turtle.fillcolor("saddlebrown")
turtle.right(90)
turtle.forward(360)
turtle.right(90)
turtle.forward(1300)
turtle.right(90)
turtle.forward(360)
turtle.right(90)
turtle.forward(650)
turtle.end_fill()
turtle.penup()
turtle.left(90)

# the grass
# up stroke
turtle.right(145)
turtle.pencolor("green3")
turtle.goto(-875, 0)
for i in range(-875, 825, 8):
    turtle.pendown()
    turtle.goto(i, 0)
    turtle.forward(500)
    turtle.penup()
turtle.goto(0, 0)
turtle.left(145)
# down stroke
turtle.right(45)
turtle.pencolor("green3")
turtle.goto(-990, -360)
for i in range(-990, 825, 8):
    turtle.pendown()
    turtle.goto(i, -360)
    turtle.forward(510)
    turtle.penup()

    # the road to the lair
turtle.goto(25, 0)
turtle.setheading(0)
for i in range(10, 100, 10):
    squareblock(i)
    turtle.right(90)
    turtle.forward(i + 5)
    turtle.left(90)
    squareblock(i)
    turtle.left(90)
    turtle.forward(i + (i * .5))
    turtle.left(90)
    turtle.forward(i + 5)
    turtle.right(180)

    # the trees on the backgroud line
turtle.goto(-625, 0)
nextSpotLeft = -625
for i in range(0, 16, 1):
    base = random.randint(8, 14)
    hight = random.randint(20, 33)
    maketree(base, hight)
    nextSpotLeft += base + 26
    turtle.goto(nextSpotLeft, 0)
turtle.goto(150, 0)
nextSpotRight = 150
for i in range(0, 14, 1):
    base = random.randint(8, 14)
    hight = random.randint(20, 33)
    maketree(base, hight)
    nextSpotRight += base + 26
    turtle.goto(nextSpotRight, 0)

# making the beholder
turtle.goto(60, 20)  # to make the body
turtle.setheading(0)
turtle.fillcolor("purple")
turtle.pencolor("purple")
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.goto(52, 20)  # to make white in eye
turtle.fillcolor("white")
turtle.pencolor("black")
turtle.pendown()
turtle.begin_fill()
turtle.circle(12)
turtle.end_fill()
turtle.penup()
turtle.goto(40, 12)  # making the puple for his eye
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.pendown()
turtle.begin_fill()
turtle.left(45)
turtle.forward(12)
turtle.right(90)
turtle.forward(12)
turtle.right(90)
turtle.forward(12)
turtle.right(90)
turtle.forward(12)
turtle.end_fill()
turtle.penup()

# making the arms
for i in range(0, 360, 30):
    turtle.goto(60, 20)
    turtle.setheading(0)
    turtle.circle(20, i)
    arm(4, "green", "yellow")

# making the flowers
# Took out grabbing user input, just made it a flat number
"""
numflowers = input("How many flowers would you like? please enter a nubmer bigger then 20")
while not numflowers.isdigit():
    numflowers = input("That was not what I asked for please try again, How many flowers would you like? please enter a nubmer bigger then 20")
while int(numflowers) < 20:
    numflowers = input("That was not what I asked for please try again, How many flowers would you like? please enter a nubmer bigger then 20")

"""
numflowers = 25

level1 = False
level2 = False
level3 = False
levelcount = 0

for i in range(0, int(numflowers), 1):
    level = random.randint(-250, -15)
    xspot = random.randint(-600, 600)
    while -150 < xspot < 150:  # so dont show up on road
        xspot = random.randint(-650, 650)
    colorran = random.randint(0, 4)

    """
    different levels
    1 /// x = 15-100,9-13,2-4,2-4,1-3
    2 /// x = 101-150,16-20,4-6,4-6,3-5
    3 /// x = 151-250,19-23,6-8,6-8,5-7
    """
    # so each run i get an even spread of flowers on levels
    if level < -14 and level >= -100 and level1 == True:  # to get new num if level 1 has a flower
        if level2 == True:
            level = random.randint(-250, -151)  # if flower in level 1 and level 2
        else:
            level = random.randint(-150, -101)  # if flower in level 1 and level 3

    if level < -101 and level >= -150 and level2 == True:  # flower in level 2
        if level1 == True:
            level = random.randint(-250, -151)  # flower in level 2 and 1
        else:
            level = random.randint(-100, -15)  # flower in level 2 and 3

    if level < -151 and level >= -250 and level3 == True:  # flower in level 3
        if level1 == True:
            level = random.randint(-150, -101)  # flower in level 3 and 1
        else:
            level = random.randint(-100, -15)  # flower in level 3 and 2

            # for level 1
    if level < -14 and level >= -100:
        turtle.goto(xspot, level)
        Rstemside = random.randint(9, 13)
        Rstemtop = random.randint(3, 4)
        Rinner = random.randint(2, 3)
        Routter = random.randint(1, 3)

        makeflower(Rstemside, Rstemtop, Rinner, Routter, colorlist[colorran], xspot, level)

        level1 = True
        levelcount += 1
        # for level 2
    if level < -101 and level >= -150:
        turtle.goto(xspot, level)
        Rstemside = random.randint(16, 20)
        Rstemtop = random.randint(5, 6)
        Rinner = random.randint(4, 5)
        Routter = random.randint(3, 5)

        makeflower(Rstemside, Rstemtop, Rinner, Routter, colorlist[colorran], xspot, level)

        level2 = True
        levelcount += 1
        # for level 3
    if level < -151 and level >= -250:
        turtle.goto(xspot, level)
        Rstemside = random.randint(19, 23)
        Rstemtop = random.randint(7, 8)
        Rinner = random.randint(6, 7)
        Routter = random.randint(5, 7)

        makeflower(Rstemside, Rstemtop, Rinner, Routter, colorlist[colorran], xspot, level)

        level3 = True
        levelcount += 1
        # to reset
    if levelcount == 3:
        level1 = False
        level2 = False
        level3 = False
        levelcount = 0

close = input("press enter to quit")
