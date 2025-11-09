import turtle

t = turtle.Turtle()

t.speed('fastest')

print("Make a portal to another dimension! How big is it?")

max_steps = input()

for x in max_steps:
    if x not in "0123456789":
        print("invalid input, enter a number")
        exit()
     
max_steps = int(max_steps)

if max_steps > 45:
    print("Woah, you're going to destroy the universe! Enter a smaller number.")
    exit()

if max_steps < 15:
    print("Aww man, your portla glitched. Try again.")
    exit()

print("Give a color from the rainbow")
color1 = input().strip().lower()
print("Give another color:")
color2 = input().strip().lower()
print("Give one last color:")
color3 = input().strip().lower()

palette = {
    "red": "#FF073A",
    "orange": "#FFA500",
    "yellow": "#FFFF33",
    "green": "#39FF14",
    "blue": "#1F51FF",
    "purple": "#BF00FF",
}

if color1 not in palette or color2 not in palette or color3 not in palette:
    print("Sorry, at least one of your colors is invalid.")
    exit()

def recursive_spiral(current_step, max_steps, counter=0):
    if current_step >= max_steps:
        return counter  
    base_length = 30
    length = base_length + (current_step * 10)

    t.color(palette[color1])
    t.forward(length)
    t.right(190)
    t.color(palette[color2])
    t.forward(length)
    t.right(190)
    t.color(palette[color3])
    t.forward(length)
    t.right(190)

    return recursive_spiral(current_step + 1, max_steps, counter + 1)

t.penup()
t.goto(-10, -10)
t.pendown()

total = recursive_spiral(0, max_steps)

print("Total recursion calls: " + str(total))