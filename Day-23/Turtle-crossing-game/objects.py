from turtle import Turtle
import random
X_COR_POSITION = 280
OBJECT_COLORS = ["orange", "purple", "Green", "Blue"]

class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cor = random.randint(-280, 240)
        self.shape("square")
        self.shapesize(0.6, 2)
        self.color(random.choice(OBJECT_COLORS))
        self.penup()
        self.position()
        self.setheading(180)
    
    def position(self):
        self.goto(X_COR_POSITION, self.y_cor)

    def move(self):
        self.forward(5)
