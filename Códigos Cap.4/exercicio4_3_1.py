import turtle, math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    turtle.mainloop()

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 10) 
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)
    turtle.mainloop()

def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()

# square(bob, 100)
# square(bob, 50)
# polygon(bob, 5, 100)
circle(bob, 50)
# arc(bob, 50, 180)
# polyline(bob, 30, 100, 1)