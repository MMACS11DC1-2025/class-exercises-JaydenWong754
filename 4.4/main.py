import turtle

turtle = turtle.Turtle()



def fractal(times):

    if times == 0:
        turtle.stamp()

    else:
        turtle.left(45)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
fractal(10)
