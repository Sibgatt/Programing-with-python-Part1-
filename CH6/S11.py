import turtle

turtle.shape("turtle")
turtle.speed(2)

for side_length in range(50,100,10): #starting from 50 the loop will continue untill 100 is finished increasing 10 each ..
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

turtle.exitonclick()