from turtle import Turtle
import random

class Scoreboard():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.goto(0, 270)

    
    def scoreUpdate(self, score, highScore):
        self.turtle.clear()
        self.turtle.write(f"Score: {score} Current High Score: {highScore}", False, align="center", font=("Arial", 24, "normal"))


    def GameOver(self, score, highScore):
        self.turtle2 = Turtle()
        self.turtle2.penup()
        self.turtle2.hideturtle()
        self.turtle2.color("white")
        self.turtle2.goto(0, 0)
        if(score>highScore):
            self.turtle2.write(f"GAME OVER! NEW HIGH SCORE!!! {score}. Current High Score: {highScore}",False, align="center", font=("Arial", 24, "normal"))
        else:
            self.turtle2.write(f"GAME OVER :( Your Score: {score}. Current High Score: {highScore}",False, align="center", font=("Arial", 24, "normal"))