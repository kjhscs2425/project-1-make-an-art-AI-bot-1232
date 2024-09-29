from turtle import *
from math import *

#initial settings
tracer(0,0)

#two main variables
length=100   #controls the size of the blocks
star_size=50 #controls the size of the star

pencolor("black")

#this function draws a block
def draw_block(block_length):

    offset=block_length/2
    angle=45
    hyp=sqrt(offset*offset+offset*offset) #hypothenuse

    pendown()

    #draw a square
    for _ in range(4):
        forward(block_length)
        right(90)
    
    #move pen into position to draw second square offset
    penup()
    right(90)
    forward(block_length/2)
    left(90)
    forward(block_length/2)

    #draw second square
    pendown()
    left(90)
    forward(block_length)
    for _ in range(4):
        right(90)
        forward(block_length)

    right(225)
    forward(hyp)
    right(225)
    forward(block_length)
    left(45)
    forward(hyp)
    right(135)
    forward(block_length)
    right(45)
    forward(hyp)
    right(45)
    forward(block_length)
    right(135)
    forward(hyp)
    right(180)
    forward(hyp)
    right(135)
    forward(block_length)
    right(90)

    penup()
#end of function draw_block

#function to draw a 5 point star
def draw_star(size):
    pendown()
    left(70)
    pencolor("black")
    begin_fill()
    for _ in range(5):
        forward(size)
        left(144)
    end_fill()
    right(70)
    penup()


#main code
#draw frist block of base
draw_block(length)
forward (length)

#draw second block of base
draw_block(length)
left(180)

#draw third block of base
forward(2*length)
left(180)
draw_block(length)

#move turtle to the second level
left(90)
forward(length)
right(90)
forward(length/2)

#draw first block of second level
draw_block(length)

#draw second block of second level
forward(length)
draw_block(length)

#move turtle to the third level
left(90)
forward(length)
right(90)
forward(length/2)
left(180)
forward(length)
left(180)
#draw block on third level
draw_block(length)

#draw stars on top
draw_star(star_size/2)
forward(length/2)
draw_star(star_size)
forward(length/2)
draw_star(star_size/2)

update()

exitonclick()