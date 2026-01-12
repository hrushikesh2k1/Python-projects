from turtle import Turtle
YCOR = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position)

    def up(self):
        if(self.ycor() < 240):
            self.goto(self.xcor(), self.ycor() + YCOR)

    def down(self):
        if(self.ycor() > -240):
            self.goto(self.xcor(), self.ycor() - YCOR)
    



