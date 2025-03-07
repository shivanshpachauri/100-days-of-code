from turtle import Turtle,Screen, setheading
import time
timmy=Turtle()
screen=Screen()
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.heading=self.segments[0]
       
    def create_snake(self):
        for position in STARTING_POSITIONS:
            screen.update()
            screen.tracer(0)
            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def movesnake(self): 
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.heading.heading()!=DOWN:
            self.heading.setheading(UP)
    def down(self):
        if self.heading.heading()!=UP:
            self.heading.setheading(DOWN)
        # pass
        # self.segments[0].setheading(90)
    def left(self):
        # pass
        if self.heading.heading()!=RIGHT:
            self.heading.setheading(LEFT)
    def right(self):
        # pass
        if self.heading.heading()!=LEFT:
            self.heading.setheading(RIGHT)