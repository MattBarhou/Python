from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.highscore = 0
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.read_highscore()
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align="center", font=("Courier", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.highscore:
            self.write_highscore(self.score)
        self.score = 0
        self.update_scoreboard()
        
    def read_highscore(self):
        with open("./Snake Game/data.txt", "r") as data:
            self.highscore = int(data.read())
            
    def write_highscore(self, score):
        with open("./Snake Game/data.txt", "w") as data:
            data.write(str(score))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))