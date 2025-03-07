from turtle import Turtle,Screen
from CustomSnake import Snake
import time
timmy=Turtle()
Snake=Snake()


screen=Screen()
timmy.speed("slow")
# screen.exitonclick()
screen.setup(width=600,height=600)
screen.bgcolor("black")

screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

screen.onkey(Snake.up,"Up")

screen.onkey(Snake.down,"Down")

screen.onkey(Snake.left,"Left")

screen.onkey(Snake.right,"Right")
# screen.update()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.movesnake()
