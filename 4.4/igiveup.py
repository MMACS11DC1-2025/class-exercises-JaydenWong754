import turtle

t = turtle.Turtle()

def fractal(times):
    if times == 0:
        return
    
    for x in range(200):
        t.forward()
        t.forward(30)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(30)
        t.right(90)