from turtle import Turtle, Screen
from math import pi, sin, cos

screen = Screen()

body = Turtle(shape="circle")
body.color('red')
body.penup()

time_t = Turtle(visible=False)  # For time output
time_t.penup()
time_t.setposition(200, 200)  # In this position I want to output variable
time_t.write("t = " + str(0))

screen.tracer(0)  # Control animation updates ourself

def Motion(A=100, omega=5, N=2):
    n = 0
    t = 0

    def x_pos(t):
        return A * cos(0.5 * omega * t)  # x

    def y_pos(t):
        return A * sin(1 * omega * t)  # Ky

    body.setposition(x_pos(t), y_pos(t))
    body.pendown()

    while n < N:
        body.setposition(x_pos(t), y_pos(t))

        t = round(t + 0.01, 2)
        time_t.undo()  # undraw the last time update
        time_t.write("t = " + str(t))  # Show the time variable t on screen
        screen.update()

        if int(round(t / (2 * pi / omega), 2)) == n + 1:
            n = n + 1

Motion()

screen.exitonclick()
