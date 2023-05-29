import turtle
tree=turtle.Turtle()
tree.screen.bgcolor("black")
tree.pensize(2)
tree.color("white")
tree.left(90)
tree.backward(100)
tree.speed(10000)
tree.shape("turtle")

def pohon(i):
    if i<10:
        return
    else:
        tree.forward(i)
        tree.color("yellow")
        tree.circle(2)
        tree.color("brown")
        tree.left(30)
        
        pohon(3*i/4)
        tree.right(60)
        pohon(3*i/4)
        tree.left(30)
        tree.backward(i)
pohon(100)
turtle.done()