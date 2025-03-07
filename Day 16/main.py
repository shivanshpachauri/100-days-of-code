# from turtle import *
# # color('blue')
# for c in ('blue','green','red'):
#     color(c)
#     left(100)
#     forward(200)
#     right(100)
#     backward(200)
from turtle import Turtle,Screen,color
timmy=Turtle()
print(timmy)
# for c in ('orange','red','green'):
#     timmy.color(c)
# timmy.color('orange')
timmy.shape("turtle")
timmy.color("red")
for c in ('orange','red','green','coral'):
    timmy.speed(1)
    timmy.color(c)
    timmy.left(100)
    timmy.forward(100)
    
    # timmyvery tired very exhaustive timmy is just a douchebag
    # timmy.right(100)
    timmy.backward(100)
    # timmy.left(100)
    timmy.fillcolor('yellow')
    timmy.fillcolor('coral')

my_screen=Screen()
print(my_screen.canvheight)

my_screen.exitonclick()