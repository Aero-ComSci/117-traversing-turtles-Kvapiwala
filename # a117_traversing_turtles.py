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

    #  starting positional and heading variables
    startx = 0
    starty = 0
    heading = 0

    #for each shape added to the my_turtle list it goes to the starting position and creates the following drawing
    for t in self.my_turtles:
      tcolor = self.turtle_colors.pop()
      t.penup()
      t.goto(startx, starty)
      t.pendown()
      t.setheading(heading)
      t.pencolor(tcolor)
      t.fillcolor(tcolor)
      t.begin_fill()
      t.right(45)     
      t.forward(50)
      t.end_fill()

    #	updates the positional variables for new starting locations
      startx = t.xcor()
      starty = t.ycor()
      heading  = t.heading()
  def __str__(self):
    Turtles = []
    for shape in self.turtle_shapes:
      Turtles.append(shape)
    return f"All the different Turtles visible are {Turtles}"

draw = Turtles()
draw.draw()
print(draw)

wn = trtl.Screen()
wn.mainloop()