import turtle as tu


#wn = tu.Screen()
foo = tu.Turtle()
foo.left(90)
foo.speed(1)

#recursion
def draw(l):
    if(l<10):
        return
    else:
        foo.forward(l)
        foo.left(30)
        draw(3*l/4)
        foo.right(60)
        draw(3*l/4)
        foo.left(30)
        foo.backward(l)

draw(100)
