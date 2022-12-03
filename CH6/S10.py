# you can draw a dash line using turtle
import turtle

turtle.speed(1)

for i in range (20):
    turtle.forward(10)
    turtle.penup()#you can use penup() to stop turtle drawing any un wanted line or mark
    turtle.forward(3)
    turtle.pendown()


turtle.exitonclick()