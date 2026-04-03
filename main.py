from turtle import *
import random



window = Screen()
window.bgcolor("black")
window.setup(600,600)

pen = Turtle()
pen.hideturtle()
pen.speed(0)



pen.color("white")
pen.up()
pen.goto(0,150)
pen.down()

sides = int(input("how many sides do you want the polygon to have").strip())
angle = 180 + (((sides - 2 ) * 180)/sides) 
length = 600/sides

if sides == 4:
    type_of_quadrilateral = input(("what type of quadrillateral?\n\n No two sides of the quadrilateral are parallel:	Unknown quadrilateral \n\nTwo sides are parallel to each other and the remaining two sides are not parallel to each other: Trapezoid\n\nNot a rectangle and each side is parallel to one other side:	Parallelogram\n\nNot a square and all four angles have the same measure:	Rectangle\nAll four sides have the same length:   Square\n\n\njust enter the first letter of which quadrilateral").strip().lower())
    if type_of_quadrilateral.startswith("t"):
        for n in range(4):
            if n in [1,2]:
                pen.left(180+60)
                
            elif n in [0,3]:
                pen.left(180+120)
            if n in [0,2,3]:
                pen.forward(length)
            if n == 1:
                pen.forward(2* length)
            
            
    elif type_of_quadrilateral.startswith("u"):
        pen.up()
        pen.home()
        pen.down()
        for n in range(3):
            pen.forward(length )
            pen.left((random.randint(30,140)))
        pen.home()
    elif type_of_quadrilateral.startswith("p"):
        for n in range(4):
            if n in [1,3]:
                pen.left(180+60)
            elif n in [2,0]:
                pen.left(180+120)
            if n in [3,1]:
                pen.forward(length+60)
            else:
                pen.forward(length)
    elif type_of_quadrilateral.startswith("r"):
        for n in range(4):
            pen.left(angle)
            if n in [1,3]:
                pen.forward(length+60)
            else:
                pen.forward(length)
    elif type_of_quadrilateral.startswith("s"):
        
        for n in range(4):
            pen.left(angle)
            pen.forward(length)
            
    else:
        print("sorry that is not a quadrilateral")
else:
    for n in range(sides):
    
        pen.left(angle)

        pen.forward(length)
window.mainloop()