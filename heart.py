import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)
t.color('red')

# Draw the heart shape
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()