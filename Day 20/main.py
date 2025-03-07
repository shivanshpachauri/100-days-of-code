from turtle import Turtle,Screen
import random
Screen=Screen()
Screen.screensize(500,400)
user_input=Screen.textinput(title="Color ",prompt="Enter a color : ")
colors=["red","yellow","green","grey","blue","black"]
turtle_index=2
y_axis=[-70,-30,0,30,60,90]
turtles=[]
for turtle_index in range(0,6):
    timmy=Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-230,y=y_axis[turtle_index])
    turtles.append(timmy)
    # timmy.fd(random.randint(0,10))
should_stop=True
if user_input:
    should_stop=False
while should_stop!=True:
    for turtle in turtles:
        if turtle.xcor()>230:
            
            if user_input==turtle.pencolor():
                print(f"Your turtle {turtle.pencolor()} has won")
            else:
                print(f"Your turtle has lost this {turtle.pencolor()} won")
            should_stop=True
        forward=random.randint(0,10)
        turtle.fd(forward)
    

Screen.exitonclick()







