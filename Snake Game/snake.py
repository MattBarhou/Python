from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]
    
        
    def create_snake(self):
        # loop through the starting positions and add a turtle to each position
        for position in STARTING_POSITIONS:
            self.add_turtle(position)
            
    def add_turtle(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle) 
        
    def extend(self):
        # Get the position of the last segment in the snake
        last_pos = self.all_turtles[-1].position()
        # Add a new segment to the snake at this position
        self.add_turtle(last_pos)

        
        
    def move(self):
        #loop through all segments and move the 2nd and 3rd segments to the position of the 1st segment
        #then move the 1st segment forward
        for s in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[s - 1].xcor()
            new_y = self.all_turtles[s - 1].ycor()
            self.all_turtles[s].goto(new_x, new_y)
        self.all_turtles[0].forward(20)
        
    def reset(self):
        #clear the old snake and move it off the screen, then create a new snake
        for s in self.all_turtles:
            s.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            

        