from turtle import Turtle
import random as rn


class Food(Turtle):
    def __init__(self):
        # self.score=0
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        random_x=rn.randint(-280, 280)
        random_y=rn.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()
    
    # def score(self):
    #     self.score = self.score+1
    #     self.write(f"your score")
    
    def refresh(self):
        random_x=rn.randint(-280, 280)
        random_y=rn.randint(-280, 280)
        self.goto(random_x, random_y)
