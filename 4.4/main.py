#import turtle graphic module
import turtle

#create turtle module
t = turtle.Turtle()

a = True

#set speed
t.speed('fastest')

#user input for size
print("Make a portal to another dimension! How big is it? 50 to 500")
  
max_steps = input()
  
#checks character by character to make sure the user input all numbers
for x in max_steps:
    if x not in "0123456789":
        print("invalid input, enter a number")
        exit()
        
max_steps = int(max_steps) #TEST ERROR : I forgot to turn the input into an integer

#input validation if too big or small
if max_steps > 501:
    print("Woah, you're going to destroy the universe! Enter a smaller number.")
    exit() #TEST ERROR : I originally had break(), which didnt work as it can only be used in for and while loops

if max_steps < 49:
    print("Aww man, your portal glitched.")
    exit()

while a == True: #while inputs to repeat the code until user inputs valid data
  #user input - ask user to pick 3 colors from rainbow
  print("Give a color from the rainbow")
  color1 = input().strip().lower() #minimize errors
  print("Give another color:")
  color2 = input().strip().lower()
  print("Give one last color:")
  color3 = input().strip().lower()
  
  #color dictionary to set hex codes for each color of the rainbow
  palette = {
      "red": "#FF073A",
      "orange": "#FFA500",
      "yellow": "#FFFF33",
      "green": "#39FF14",
      "blue": "#1F51FF",
      "purple": "#BF00FF",
  }
  
  #check if the users input matches a color in the dictionary
  if color1 not in palette or color2 not in palette or color3 not in palette:
      print("Sorry, at least one of your colors is invalid.")
  
  else:
    a = False
    break
#recursive function
def recursive_spiral(current_step, max_steps, total_calls):
    """
    draws a colorful star recursively based on users input for size and color
    VARIABLE EXPLANATION
    current_step: which step of recursion program is on
    max_steps: total number of steps requested by user
    total_calls: counts number of segments
    """
    
    #base case -stops recursion when reached the maximum amount of steps
    if current_step >= max_steps:
        return total_calls

    #increases line for each step
    base_length = 30
    length = base_length + (current_step * 5)

    if length > 5500: #second base case
        return total_calls
    
    #draw star with chosen color
    t.color(palette[color1])
    t.forward(length)
    t.right(190)
    t.color(palette[color2])
    t.forward(length)
    t.right(190)
    t.color(palette[color3])
    t.forward(length)
    t.right(190)

    #recursive call - move to next step and increase counter by one
    return recursive_spiral(current_step + 1, max_steps, total_calls + 1)

#turtle start position
t.penup()           #lift to move to position
t.goto(-10, -10)    #go to position
t.pendown()         #pen down to prepare to draw

#run it
total = recursive_spiral(0, max_steps, 0)

t.penup()
t.goto(0, 0)

#output
print("Total recursion calls: " + str(total))  #count how many times recursio                                                                                                                                                                                                                                                     print("Total recursion calls: "