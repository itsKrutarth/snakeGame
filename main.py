from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtle1 = Turtle("square")
turtle1.color("white")
turtle2 = Turtle("square")
turtle2.color("white")
turtle2.goto(-20, 0)
turtle3 = Turtle("square")
turtle3.color("white")
turtle3.goto(-40, 0)

turtle1

screen.exitonclick()