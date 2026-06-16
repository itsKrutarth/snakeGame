import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
game_is_on = True


snake = Snake()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

while game_is_on:
    time.sleep(0.5)
    snake.snakeMove()
    screen.update()


screen.exitonclick()