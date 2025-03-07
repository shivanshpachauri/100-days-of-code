from turtle import Turtle, Screen
import turtle
import random
timmy=Turtle()
timmy.shape("turtle")
def randomchoice():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r/255, g/255, b/255)
    return color
for i in range(0,12):
    timmy.color(randomchoice())
    timmy.circle(50)
    timmy.left(30)
Screen=Screen()
Screen.exitonclick()
turtle.done()