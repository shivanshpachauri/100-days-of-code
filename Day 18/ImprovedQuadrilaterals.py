from turtle import Turtle,Screen

class Quad:
    def __init__(self):
        self.timmy=Turtle()
        self.i=0
        self.timmy.shape("turtle")        
        
    def exec(self,side):
        color=["red","blue","green","maroon","sandybrown","magenta","chocolate","purple"]
        
        angle=360/side
        for _ in range(side):
            # print(color[i])
            self.timmy.color(color[self.i])
            self.timmy.fd(100)
            self.timmy.left(angle)
            self.timmy.fd(100)
        self.i=self.i+1
    def sides(self):
        for i in range(3,11):
            # print(i)
            self.exec(i)
        


quad=Quad()
quad.sides()


Screen=Screen()
Screen.screensize(2000,1500)
Screen.exitonclick()