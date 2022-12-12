import turtle

turtle.speed(2)
turtle.color('blue')

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)



triangle(int(input('Enter the length :')))

turtle.exitonclick()