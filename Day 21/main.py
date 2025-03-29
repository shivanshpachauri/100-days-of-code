from turtle import Turtle,Screen
from CustomSnake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
Food=Food()
ScoreBoard=ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.heading.distance(Food)<15:
        Food.refresh()
        snake.extend()
        ScoreBoard.increase_ScoreBoard()
    if snake.heading.xcor()>280 or snake.heading.xcor()<-280 or snake.heading.ycor()>280 or snake.heading.ycor()<-280:
        game_is_on=False
        ScoreBoard.game_over()
    for segment in snake.segments[1:]:
        # if segment==snake.heading:
        #     pass
        if snake.heading.distance(segment)<10:
            ScoreBoard.game_over()
            # game_is_on=False