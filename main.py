#main.py
#initial imports
import turtle
turtle.tracer(0,0)
turtle.speed(10)
#defining key variable
    #forward a certian size length
forward = 50
#define functions
    #draw square
def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    #draw circle
def draw_circle():
    for i in range(180):
        turtle.forward(0.3)
        turtle.left(1)
    #draw triangle
def draw_ear():
    turtle.right(60)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(160)
def draw_eye():
    print(8)
#call funnctions

#nose of the dog
turtle.forward(40)
turtle.right(60)
turtle.forward(20)
turtle.right(30)
turtle.forward(20)
turtle.right(40)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.right(45)
turtle.forward(20)
turtle.right(20)
turtle.forward(25)
#nose frame of dog location
turtle.right(75)
turtle.forward(40)
turtle.penup()
turtle.forward(40)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(53)
turtle.left(90)
#nose frame drawing
turtle.pendown()
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(40)
turtle.left(70)
turtle.forward(210)
turtle.left(135)
turtle.forward(205)
turtle.left(65)
turtle.forward(40)
turtle.left(45)
turtle.forward(20) 
turtle.left(55)
turtle.forward(45)
#going to bottom of dog
turtle.penup()
turtle.left(135)
turtle.left(80)
turtle.forward(200)
#drawing outline of the dog
turtle.pendown()
turtle.left(90)
turtle.forward(200)
turtle.left(120)
turtle.forward(275)
turtle.left(180)
turtle.forward(275)
turtle.left(180)
turtle.left(60)
turtle.forward(388)
turtle.left(240)
turtle.forward(240)
#bandanda of the dog
turtle.left(180)
turtle.forward(120)
turtle.left(80)
turtle.forward(170)
turtle.left(80)
turtle.forward(180)
turtle.left(140)
turtle.forward(273)
turtle.left(180)
turtle.forward(120)
turtle.left(270)
turtle.penup()
turtle.forward(60)
turtle.right(90)
turtle.forward(50)
turtle.write("Sailor", font=("Verdana",
                                    45, "normal"))
turtle.left(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(60)
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
#Draw mouth
turtle.pendown()
turtle.forward(20)
turtle.left(180)
turtle.forward(90)
turtle.left(180)
turtle.forward(55)
turtle.forward(7)
#Draw tongue
turtle.left(90)
draw_circle()
#draw full outline
turtle.penup()
turtle.left(180)
turtle.forward(140)
turtle.left(90)
turtle.forward(180)
turtle.left(120)
turtle.forward(130)
turtle.right(60)
turtle.pendown()
turtle.forward(175)
turtle.left(60)
turtle.forward(150)
turtle.left(20)
turtle.forward(100)
turtle.left(40)
turtle.forward(150)
turtle.left(40)
turtle.forward(100)
turtle.left(20)
turtle.forward(150)
turtle.left(60)
turtle.forward(195)
turtle.left(120)
turtle.penup()
turtle.forward(130)
turtle.left(10)
turtle.forward(90)
#eye number one
turtle.pendown()
turtle.left(80)
turtle.forward(45)
turtle.left(20)
turtle.forward(40)
turtle.left(60)
turtle.forward(40)
turtle.left(80)
turtle.forward(40)
turtle.left(50)
turtle.forward(40)
turtle.left(40)
turtle.forward(55)
turtle.right(45)
turtle.penup()
turtle.forward(73)
#other eye
turtle.pendown()
turtle.right(20)
turtle.forward(45)
turtle.left(20)
turtle.forward(40)
turtle.left(60)
turtle.forward(40)
turtle.left(80)
turtle.forward(40)
turtle.left(50)
turtle.forward(40)
turtle.left(40)
turtle.forward(55)
turtle.right(45)
turtle.penup()
turtle.forward(50)
turtle.right(90)
turtle.forward(172)
turtle.left(90)
turtle.forward(65)
#draw ear left
draw_ear()
#draw ear right
turtle.left(180)
turtle.forward(160)
turtle.right(140)
turtle.forward(100)
turtle.left(60)
turtle.forward(150)
turtle.left(60)
turtle.pendown()
turtle.forward(100)
turtle.right(140)
turtle.forward(160)

#draw bubbles and foam blocks
circle_len = 1 #circle radius can take in values to change the radius into different sized bubbles
block_len = 25 #block length can take in different values to change how big the foam squares are
def draw_bubble (circle_len):
    for i in range(365):
        turtle.forward(circle_len)
        turtle.left(1)
def draw_block (block_len, tilt):
    turtle.left(tilt)
    for i in range(4):
        turtle.forward(block_len)
        turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.pendown()
draw_bubble(1)
turtle.penup()
turtle.left(60)
turtle.forward(200)
turtle.pendown()
draw_bubble(0.5)
turtle.penup()
turtle.right(100)
turtle.forward(150)
turtle.pendown()
draw_block(100, 90)
turtle.penup()
turtle.left(40)
turtle.forward(200)
turtle.pendown()
draw_block(100, 10)
turtle.penup()
turtle.left(90)
turtle.forward(1100)
#draw a few through changing loop
turtle.pendown()
for i in range(3):
    turtle.pendown()
    draw_bubble(i)
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
for i in range(3):
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    draw_block(block_len, 30)





turtle.update()
turtle.exitonclick()