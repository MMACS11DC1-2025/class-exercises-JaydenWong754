import turtle

t = turtle.Turtle()
t.speed('fastest')

print("Make a star! How big is it?")
max_steps = int(input())

if max_steps > 45:
  print("woah your going to destroy the milky way, enter a smaller number")
  exit()
  
if max_steps < 15:
  print("aww man your star merged intop a black hole. Try again")
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
  print("sorry, at least one of your colors is invalid")
  exit()

def recursive_spiral(current_step, max_steps, counter=1):
    if current_step >= max_steps:
        return counter

    base_length = 30
    length = base_length + (current_step * 10)

    t.color(color1)
    t.forward(length)
    t.right(190)
    t.color(color2)
    t.forward(length)
    t.right(190)
    t.color(color3)
    t.forward(length)
    t.right(190)

    return recursive_spiral(current_step + 1, max_steps, counter + 1)

t.penup()
t.goto(-10, -10)
t.pendown()

total = recursive_spiral(0, max_steps)
print("Total recursion calls:" + str(total))