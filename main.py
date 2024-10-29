from turtle import *
from math import *

#initial settings
tracer(0,0)

#two main variables
#length controls the size of the blocks, values can be any positive integer
length=int(textinput("Cubelength","Enter length of cube:"))
#star size controls the size of the star, values can be any positive integer
star_size=int(textinput("Starsize","Enter size of stars:"))



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
    for i in range(4):
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
    left(72)
    pencolor("black")
    begin_fill()
    for i in range (5):
        forward(size)
        left(144)
    end_fill()
    right(72)
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

#draw 3 stars on top
#loop where the loop variable changes something in the design
#i=1 draws a big star, i=2 draws a small star
for i in (2,1,2):
    draw_star(star_size/i)
    forward(length/2)
write("I FINISHED MY HOMEWORK =)")

#get rid of cursor
penup()
forward(10000)
update()






exitonclick()