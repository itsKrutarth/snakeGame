import time
from turtle import Turtle

TURTLE_POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.turtles = []
        self.createSnake()
        
        
    def createSnake(self):
        for pos in TURTLE_POS:
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(pos)
            turtle.speed(10)
            self.turtles.append(turtle)

    def snakeMove(self):
        for i in range(len(self.turtles)-1, 0, -1):
            x =self.turtles[i-1].xcor()
            y= self.turtles[i-1].ycor()
            self.turtles[i].goto(x, y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def Up(self):
        if(self.turtles[0].heading()!=270):
            self.turtles[0].setheading(90)
    
    def Down(self):
        if(self.turtles[0].heading()!=90):
            self.turtles[0].setheading(270)
    
    def Left(self):
        if(self.turtles[0].heading()!=0):
            self.turtles[0].setheading(180)
    
    def Right(self):
        if(self.turtles[0].heading()!=180):
            self.turtles[0].setheading(0)

    
            
