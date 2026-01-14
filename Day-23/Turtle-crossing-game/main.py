from turtle import Turtle, Screen
import time
from jack import Jack
from objects import Object
import random
from levels import Level

screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.setup(600, 600)

jack = Jack()
level = Level()

screen.onkey(jack.up, "Up")

game_on = True
object_list = []

while game_on:
    time.sleep(level.move_speed)
    screen.listen()

    # create objects
    if(random.randint(4,5) == 5):
        new_object = Object()
        object_list.append(new_object)

    # Moving the object
    for object in object_list:
        object.move()


    # Change level
    if(jack.ycor() > 240):
        level.next_level()
        jack.reset_position()

        
    
    # detect collision with turtle
    for object in object_list:
        if(jack.distance(object) < 10):
            level.game_over()
            game_on = False
        
    
    screen.update()

    
screen.exitonclick()
