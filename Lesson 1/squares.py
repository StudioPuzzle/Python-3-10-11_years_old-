import turtle
t = turtle.Pen()
for i in range(12):
    t.pencolor("red")
    for x in range(4):
        t.forward(50)
        t.left(90)
    t.left(20)
