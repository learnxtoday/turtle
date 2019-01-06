import turtle

# function to make a square. Initialize a turtle instance, and pass it in the function. 
def square(bob):
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()

# moves cursor down to create a new shape
def moveDown(bob):
    bob.penup()
    bob.forward(150)
    bob.pendown()


bob = turtle.Turtle()
bob.color("black", "red")
square(bob)

moveDown(bob)

bob.color("black", "green")
square(bob)


turtle.done()
