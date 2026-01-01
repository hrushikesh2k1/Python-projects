## Create a Hirst painting using turtle graphics
```
pip install colorgram.py
```

```
# import colorgram

# colors = colorgram.extract("hirst.jpg", 30)
# rgb_colors = []

# for i in range(30):
#     color = colors[i]
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

from turtle import Turtle, Screen
screen = Screen()

timmy = Turtle()
screen.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.right(150)
timmy.forward(300)
timmy.left(150)
timmy.dot(20, color_list[0])
position = timmy.pos()


count = 0
for i in range(3):
    for j in range(10):
        color = color_list[count]
        timmy.forward(50)
        timmy.dot(20, color)
        count+=1
    timmy.setposition(-259.81, (i+1)*50-150.00)



screen.exitonclick()
```

output:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/33f1c1aa-5156-4f8a-849e-e7ecb03e7e9f" />
