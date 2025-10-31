import turtle

t = turtle.Turtle()

max_steps = 60

def recursive_spiral(current_step, max_steps):
    if current_step >= max_steps:
        return
    
    base_length = 30
    length = base_length + (current_step * 10)

    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)

    recursive_spiral(current_step + 1, max_steps)

t.penup()
t.goto(-10, -10)
t.pendown()