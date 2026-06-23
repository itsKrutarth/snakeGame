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
highScore = 0
with open("highScore.txt", mode="r") as file:
    highScore = int(file.read())

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
        scoreboard.scoreUpdate(score=score, highScore=highScore)
    if(snake.getHead().xcor()>280 or snake.getHead().xcor()<-280 or snake.getHead().ycor()>280 or snake.getHead().ycor()<-280):
        game_is_on= False
        scoreboard.GameOver(score=score, highScore=highScore)
    for turtle in snake.turtles[1:len(snake.turtles)]:
        # if (turtle == snake.getHead()):
        #     pass
        if(snake.getHead().distance(turtle)<10):
            game_is_on= False
            scoreboard.GameOver(score=score, highScore=highScore)
            break
    screen.update()
    if(score>highScore):
        highScore=score

with open("highScore.txt", mode="w") as file:
    file.write(str(highScore))

screen.exitonclick()