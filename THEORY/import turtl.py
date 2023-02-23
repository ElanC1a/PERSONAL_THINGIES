import turtle
#turtle.shape("turtle") #5-6 shapes
#turtle.forward(100) 
#turtle.left(100)
#turtle.forward(100)
#turtle.mainloop()
#turtle.penup() / pendown()

t=turtle.Turtle()
amount=int(input("How many times:"))
size=30
angle=1
def circle(size):
    for i in range (4):
        t.speed(0)
        t.forward(size)
        t.left(90)
        
for i in range(amount):
    circle(size)
    size=size+0.6
    t.right(angle)
    angle=angle+0.8

turtle.mainloop()