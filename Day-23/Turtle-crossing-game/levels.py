from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-240, 280)
        self.hideturtle()
        self.level = 1
        self.move_speed = 0.1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 10, "normal"))
    
    def next_level(self):
        self.level += 1
        self.move_speed *= 0.9
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="Center", font=("Courier", 20, "normal"))
