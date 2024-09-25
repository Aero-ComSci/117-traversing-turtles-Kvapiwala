#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles

class Turtles:
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

  def __init__(self):
    self.my_turtles = []



  #adds shapes to my_turtle list by iterating through the shapes list
  def draw(self):
    for s in self.turtle_shapes:
      t = trtl.Turtle(shape=s)
      self.my_turtles.append(t)

    #  starting positional variables
    startx = 0
    starty = 0

    #for each shape added to the my_turtle list it goes to the starting position and creates the following drawing
    for t in self.my_turtles:
      t.goto(startx, starty)
      t.right(45)     
      t.forward(50)

    #	updates the positional variables for new starting locations
      startx = t.xcor()
      starty = t.ycor()


draw = Turtles()
draw.draw()

wn = trtl.Screen()
wn.mainloop()