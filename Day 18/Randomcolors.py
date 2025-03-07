import turtle as t
import random
from turtle import Screen
# from random import choice
def randomchoice():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b
color=["red","blue","green","maroon","sandybrown","magenta","chocolate","purple"]
r,g,b=randomchoice()
print(r,g,b)
for i in range(100):
    r,g,b=randomchoice()
    # r=tostring(r)
    color=(r,g,b)
    t.color(color)
    steps = random.randint(1,100)
    angle = 30
    t.fd(steps)
    t.left(angle)


Screen=Screen()
Screen.exitonclick()