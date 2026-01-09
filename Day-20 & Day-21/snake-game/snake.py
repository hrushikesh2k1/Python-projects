from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20,0) , (-40,0)] # CONSTANTS
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT =180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(pos)
            self.segments.append(new_seg)
        
    def extend(self):
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(self.segments[-1].pos())
            self.segments.append(new_seg)
    
    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[seg-1].xcor()
            ycor = self.segments[seg-1].ycor()
            self.segments[seg].goto(xcor, ycor)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if(self.segments[0].heading() != DOWN):
            self.segments[0].setheading(UP)

    def down(self):
        if(self.segments[0].heading() != UP):
            self.segments[0].setheading(DOWN)
    
    def right(self):
        if(self.segments[0].heading() != LEFT):
            self.segments[0].setheading(RIGHT)

    def left(self):
        if(self.segments[0].heading != RIGHT):
            self.segments[0].setheading(LEFT)

