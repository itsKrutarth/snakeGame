from turtle import Turtle
import random

class Scoreboard():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.goto(0, 270)
    
    def scoreUpdate(self, score):
        self.turtle.clear()
        self.turtle.write(f"Score: {score}", False, align="center", font=("Arial", 24, "normal"))