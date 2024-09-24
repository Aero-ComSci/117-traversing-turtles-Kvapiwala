#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
trtl.penup()

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#adds shapes to my_turtle list by iterating through the shapes list
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  starting positional variables
startx = 0
starty = 0

#for each shape added to the my_turtle list it goes to the starting position and creates the following drawing
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(45)     
  t.forward(50)

#	updates the positional variables for new starting locations
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()