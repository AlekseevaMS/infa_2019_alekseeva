import turtle

turtle.shape('turtle')
n=5
k=50
for i in range(0, 250):
    turtle.forward(k*n/360)
    turtle.right(n)
    k+=10


turtle.exitonclick()
