[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/K3waziIG)
# Activity 1.1.7

* Utilize this read me to showcase the project.
* Be sure to read and use the markdown here:
[MarkDown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Stack Edit for markdown editing](https://stackedit.io)

* Write a description of what the program does, who is it for?
---




### [Book Link](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/88fb6ad306ee44d0b055d9008ace8e80)


## Questions about the Activity as you work. 
```
Step 5: The loop prints every value in the list new_list. This is because the loop ends up iterating through every value and then prints that value.
step 6:
   a. Print(new_list) prints all values in one line whilst the for loop prints each value in a new line.
   b. The loop iterate for the same amount of times as the amount of values in the list, so 5 times.
   c. The loop variable is animal
step 16:
   a. If you remove a color from the color list an error happens whilst iterating through, this is because the iteration is based off the amount of turtles there are in the turtle_shapes list, hence there must be a matching amount of colors, when it gets to the last shape the loop fails to pop another color because it does not exist.
   b. Removing a shape from the turtle list does not cause an error, rather it just iterates for less amount of times. Because our loop is based on the shapes in the list, if you remove one it simply iterates one time less.
```
## important note about the __str__ method:
The colors cannot be displayed since we are popping all the values out of that list in the loop, hence when trying to return that list, it just displays an empty list. So in the __str__ method I have only returned the turtles present in the image.(Baez Approved) 


#### Description Of The App according to User Story

` This app simply draws a spiral pattern increasing in size using different turtle shapes and colors based of a data list that contains those values. It is done by using loops and iterating through for item in the lists and using positional, heading, and sizing variables to scale the spiral. This program is for anyone wanting to learn how to use loops and how you can use other variables to determine drawing factors in Turtle. 

# Include a video of the result of the code at speed 0 or Fast. Be sure to make it available for me to see.

I staged the video from git and I dont know why it does not bypass the file limit, it is still under 25mb limit but here it is linked here:
 https://github.com/Aero-ComSci/117-traversing-turtles-Kvapiwala/blob/main/20240926_170058.mp4 
## For Regrades use the Feedback and @baeztheprog on your commit messages.
