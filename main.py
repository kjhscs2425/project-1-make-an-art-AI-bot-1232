
from turtle import *
# number cube 1 
# speed(10000000000)
tracer(0,0)
Y=5
pencolor("black")


def justin():
    print("hello Naveen")

def draw_block():
    for _ in range(4):
        forward(100)
        right(90)
    penup()
    right(90)
    forward(50)
    left(90)
    forward(50)
    pendown()
    left(90)
    forward(100)
    for _ in range(4):
        right(90)
        forward(100)

    right(180)
    forward(100)
    right(45)
    forward(72)
    right(135)
    forward(101)
    right(45)
    forward(70)
    right(45)
    forward(100)
    right(90) 
    forward(100)
    right(45)
    forward(70)
    right(45)
    forward(100)
    right(180)
    forward(100)
    left(90)
    forward(100)
    right(45)
    forward(70)
    # move back to start position
    backward(70)
    right(45)
    backward(100)

draw_block()
# number cube 2
# move to where next block starts
forward(100)
draw_block()

# number cube 3 
backward(200)
draw_block()

# number cube 4
# move to where into the middle of the block
pencolor("black")
right(90)
left(90)
left(90)
backward(100)
forward(100)
right(90)
forward(100)
left(90)
left(90)
forward(50)
right(90)
penup()
forward(50)
right(90)
forward(50)
left(90)
right(90)
# move to wehre into the middle of the block 
penup()
forward(100)
left(90)
left(90)
forward(-Y)
draw_block()
right(90)
forward(100)
right(90)
left(45+180)
forward(73)
left(45)
left(90)
draw_block()
# penup()
# forward(2)
# penup()
# right(90)
# forward(100)
# left(90)
# forward(50)
# right(270)
# right(90)
# penup()
# right(900+90)
# right(180)
# forward(100)
# right(270)
# left(90)
# right(180)
# forward(100)
# right(90)
# forward(50)
# right(90)
# forward(100)
# forward(50)
# left(90)
# forward(10)
# right(90)
# right(90)
# left(90)
# forward(100)
# cube number 6
pencolor("black")
left(90)
penup()
forward(100)
left(90)
forward(50)
right(180)
draw_block()
print("hello Naveen")
#Draws a 5 point star 
penup()
forward(25)
pendown()
forward(25)
left(70)
pencolor("black")
begin_fill()
for _ in range(5):
    forward(200)
    left(144)
end_fill()






update()
exitonclick()