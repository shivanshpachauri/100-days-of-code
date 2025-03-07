from turtle import Turtle,Screen
Screen=Screen()
timmy=Turtle()
def forwards():
    timmy.fd(100)

def backwards():
    timmy.bk(100)

def left():
    timmy.left(90)

def right():
    timmy.right(90)    
def clearscreen():
    Screen.reset()

Screen.onkey(forwards,'w')

Screen.onkey(backwards,'s')

Screen.onkey(left,'a')

Screen.onkey(right,'d')

Screen.onkey(clearscreen,'c')

Screen.listen()
# timmy.fd(100)


Screen.exitonclick()







