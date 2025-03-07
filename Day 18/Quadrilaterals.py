from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
def square():
    
    for _ in range(4):
        timmy.color("red")
        timmy.fd(100)
        timmy.left(90)
        timmy.fd(100)
def triangle():
    # triangle
    # 360/3 =120
    for _ in range(3):
        timmy.color("blue")
        timmy.fd(100)
        timmy.left(120)
        timmy.fd(100)
def pentagon():
    # pentagon
    # 360/5=72
    for _ in range(5):
        timmy.color("green")
        timmy.fd(100)
        timmy.left(72)
        timmy.fd(100)
def hexagon():
    # hexagon
    # 360/6=60
    for _ in range(6):
        timmy.color("sandybrown")
        # coldplay
        timmy.fd(100)
        timmy.left(60)
        timmy.fd(100)
def heptagon():
    # heptagon
    # 360/7=51.something
    for _ in range(7):
        timmy.color("purple")
        timmy.fd(100)
        timmy.left(51.4285714286)
        timmy.fd(100)
def octagon():
    # octagon
    # 360/8=45
    for _ in range(8):
        timmy.color("maroon")
        timmy.fd(100)
        timmy.left(45)
        timmy.fd(100)
def nonagon():
    # octagon
    # 360/9=40
    for _ in range(9):
        timmy.color("magenta")
        timmy.fd(100)
        timmy.left(40)
        timmy.fd(100)
def decagon():
    # octagon
    # 360/10=36
    for _ in range(10):
        timmy.color("chocolate")
        timmy.fd(100)
        timmy.left(36)
        timmy.fd(100)
square()
triangle()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()



Screen=Screen()
Screen.screensize(2000,1500)

Screen.exitonclick()