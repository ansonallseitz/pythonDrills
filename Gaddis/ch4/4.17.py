#drawl this start of david type start thing with the turtle. 

import turtle
turtle

START_X = 200
START_Y = -50
NUM_LINES = 16
LINE_LENGTH = 400
ANGLE = 140
ANIMATION_SPEED = 10

#move the turtle to its initial position

turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

#turtle speed
turtle.speed(ANIMATION_SPEED)

for i in range(NUM_LINES): 
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)
