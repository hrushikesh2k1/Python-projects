from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    
    # detect the collision with food
    if(snake.head.distance(food) < 15):
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_on = False
        score.game_over()

    # detect collision with own tail
    for segment in snake.segments[1:]:
        if(snake.head.distance(segment) < 10):
            game_on = False
            score.game_over()


screen.exitonclick()
