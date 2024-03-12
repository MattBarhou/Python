from turtle import Turtle, Screen
from paddle import Paddle

p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))


s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)

s.listen()


s.onkey(p1.up, "w")
s.onkey(p1.down, "s")
s.onkey(p2.up, "Up")
s.onkey(p2.down, "Down")










s.exitonclick()