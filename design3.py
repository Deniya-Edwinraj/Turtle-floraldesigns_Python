import turtle as t
t.speed(0)
t.bgcolor("black")
t.pensize(2)

for i in range(20):
    for j in range(9):
        for k in range(2):
            t.pencolor("yellow")
            t.circle(40+i*5,90)
            t.forward(100)
            t.left(90)
        t.left(45)
t.done()