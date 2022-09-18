import turtle
count = 0
while (count <= 5):
    turtle.penup()
    turtle.goto(0,count * 100)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1
turtle.left(90)
count = 0
while (count <= 5):
    turtle.penup()
    turtle.goto(count * 100,0)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1
