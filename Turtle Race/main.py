from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


screen = Screen()
screen.setup(500,400)
user_choice = screen.textinput("Bet Now!", prompt="Which turtle will win the race? Enter a color: ").lower()
all_turtles = []

# Create 6 turtles and set their position to be at the left of the window at different heights
for _ in range(6):
    t = Turtle("turtle")
    t.color(colors[_])
    t.penup()
    t.goto(-220, 100 - 40 * _)
    all_turtles.append(t)
    

#If the user input is not empty, start the loop
if user_choice:
    start_race = True
    
while start_race:
    #loop through all 6 turtles and move them forward by a random distance, if any turtle reaches the right side of the window, stop the game
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            start_race = False
            winner = turtle.color()[0]
            screen.title(f"The winner is {winner}!")
            if winner == user_choice:
                print(f"You won! The winning turtle is {winner}.")
            else:
                print(f"You lost! The winning turtle is {winner}.") 
        distance = random.randint(0, 10)
        turtle.forward(distance)
    


screen.listen()
screen.exitonclick()
