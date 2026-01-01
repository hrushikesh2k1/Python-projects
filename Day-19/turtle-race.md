## Turtle Race Game (Python)

This project is a simple Turtle Graphics race game built using Python’s turtle module. Two turtles race across the screen, and the user guesses which turtle will win before the race starts.

```
from turtle import Turtle, Screen
from random import random, choice

timmy = Turtle()
tomy = Turtle()

timmy.shape("turtle")
timmy.color("red")

tomy.shape("turtle")
tomy.color("green")

screen = Screen()
screen.setup(width=500, height=400)

timmy.penup()
timmy.goto(-500/2+10, 0)
tomy.penup()
tomy.goto(-500/2+10, 50)

f = [1,2,3,4,5,6,7,8,9,10]

timmy_xcor = timmy.xcor()
tomy_xcor = tomy.xcor()

My_choice = screen.textinput("Which turtle wins the race?", "name of the player")

while(timmy_xcor <= (500/2-20) and tomy_xcor <= (500/2-20)):
    timmy_xcor = timmy.xcor()
    tomy_xcor = tomy.xcor()
    timmy.forward(choice(f))
    tomy.forward(choice(f))

if(timmy.xcor() >= (500/2-20)):
    answer = "timmy"
else:
    answer = "tomy" 
    
if(My_choice == answer):
    print("You win!")
else:
    print("you lose! Better luck next time:)")


screen.exitonclick()
```

outputs:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a25a3961-c12a-4484-80d4-0cd35db3e2fb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/aa3d00a6-fed0-44a9-80cc-d12be003369f" />

