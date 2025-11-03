import turtle

t = turtle.Turtle()

t.speed('fastest')



print("Make a star! How big is it?")

max_steps = int(input())

print("what colors?")

def recursive_spiral(current_step, max_steps):
    palette = {"blue": "#2ABCFF", "pink": "#FF1ED6", "green": "#28FC4B"}

    if current_step >= max_steps:
        return

    base_length = 30
    length = base_length + (current_step * 10)
    
    t.color(palette["blue"])
    t.forward(length)
    t.right(190)
    t.color(palette["pink"])
    t.forward(length)
    t.right(190)
    t.color(palette["green"])
    t.forward(length)
    t.right(190)

    recursive_spiral(current_step + 1, max_steps)
    
t.penup()
t.goto(-10, -10)
t.pendown()

recursive_spiral(0, max_steps)