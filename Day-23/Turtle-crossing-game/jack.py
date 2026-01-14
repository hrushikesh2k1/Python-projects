from turtle import Turtle

class  Jack(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def up(self):
        self.forward(25)

    def reset_position(self):
        self.goto(0, -280)
