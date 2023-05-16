from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Your score: {self.score}",align="center", font=("arial",15,"normal"))
        
    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER",align="center", font=("arial",20,"normal"))
        self.hideturtle()
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()