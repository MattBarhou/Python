from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def rotate_clockwise():
    t.right(10)


def rotate_counter_clockwise():
    t.left(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=rotate_counter_clockwise)
screen.onkey(key="Right", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
