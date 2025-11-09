import turtle

t = turtle.Turtle()
amt = int(input("How many times do you want it to repeat? "))

def fractal(count):
    amt = int(input("How many times do you want it to repeat? "))
    if count > amt:
        return
    count = 0
    for x in range(200):
        t.forward(30 + count)
        t.right(90)
        t.forward(30 + count)
        t.right(90)
        t.forward(30 + count)
        t.right(90)
        count += 10
fractal(amt)