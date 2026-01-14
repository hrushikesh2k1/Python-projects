from turtle import Turtle
ALIGNMENT = "left"
FONT = ("times roman", 10, "normal")
HIGH_SCORE = open("data.txt").read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.hideturtle()
        self.goto(-50, 280)
        self.pensize(20)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game is Over", align="center", font=FONT)
        if(self.score > int(HIGH_SCORE)):
            open("data.txt", "w").write(str(self.score))
