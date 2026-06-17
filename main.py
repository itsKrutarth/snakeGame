import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreBoard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
game_is_on = True


snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

while game_is_on:
    time.sleep(0.2)
    snake.snakeMove()
    if(snake.getHead().distance(food)<15):
        score=score+1
        food.refresh()
        snake.addSegment()
        scoreboard.scoreUpdate(score=score)
    if(snake.getHead().xcor()>280 or snake.getHead().xcor()<-280 or snake.getHead().ycor()>280 or snake.getHead().ycor()<-280):
        game_is_on= False
        scoreboard.GameOver(score=score)
    for turtle in snake.turtles:
        if (turtle == snake.getHead()):
            pass
        elif(snake.getHead().distance(turtle)<10):
            game_is_on= False
            scoreboard.GameOver(score=score)
            break
    screen.update()


screen.exitonclick()