from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
for _ in range(10):     
    timmy.fd(10)
    timmy.pendown()
    timmy.fd(10)
    timmy.penup()
# timmy.showturtle()

Screen=Screen()
Screen.exitonclick()