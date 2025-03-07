from random import choice
from turtle import Screen,Turtle
import turtle
timmy=Turtle()
timmy.shape("turtle")
Screen=Screen()
Screen.colormode(255)

color=[ (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120)]
def colors():
    for i in color:
        r=i[0]
        g=i[1]
        b=i[2]
        timmy_color=(r,g,b)
        yield timmy_color
        # timmy.color(timmy_color)
        
def movement():
    alternate=False
    timmy.speed("fastest")
    timmy.penup()
    timmy.goto(-260, -260)
    
    for j in range(10):
        
        for i in range(9):
            # print(type(choice(color)))
            timmy.color(choice(color))
            # colors()
            # timmy.color(colors())
            timmy.pendown()
            timmy.dot(20)
            
            timmy.penup()
            timmy.fd(50)
        if(alternate!=True):
            timmy.dot(20)
            timmy.left(90)
            timmy.fd(50)
            timmy.left(90)
            alternate=True
        else:
            timmy.dot(20)
            timmy.right(90)
            timmy.fd(50)
            timmy.right(90)
            alternate=False
        # timmy.left(90)
movement()




Screen.exitonclick()
turtle.done()