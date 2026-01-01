## Create a Etch-a-Sketch app.
In this we used "Event listners" concept in turtle graphics.

```
# Build a Etch-a-Sketch app using screen listners
# w= Forward, S= Backwards, A= counter-clockwise, D= clockwise, C= clear drawing


from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(50)
def backwards():
    timmy.backward(50)
def counter_clockwise():
    timmy.left(10)
def clockwise():
    timmy.right(10)
def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()


screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")

screen.listen()

screen.exitonclick()
```
output:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/00ea2241-5169-41c7-a257-8f15d6c69c91" />
