import turtle

turtle.shape('turtle')
n=50
for i in range(0,8):
    for j in range(0, 4):
        turtle.right(90)
        turtle.forward(n)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    n+=20
    turtle.pendown()
    

turtle.exitonclick()
