from turtle import Turtle  # Import the Turtle module for creating graphical elements

MOVE_DISTANCE = 20  # Distance to move the snake in each step
UP = 90  # Direction code for moving up
DOWN = 270  # Direction code for moving down
LEFT = 180  # Direction code for moving left
RIGHT = 0  # Direction code for moving right

class Snake:
    def __init__(self):
        # Initialize the snake
        self.starting_body_length = 3  # Default value for the starting length of the snake
        self.body_snake = []  # List to store the segments of the snake
        self.create_snake()  # Create the initial segments of the snake
        self.head = self.body_snake[0]  # Set the head of the snake

    def create_snake(self):
        # Create the initial segments of the snake
        for i in range(self.starting_body_length):
            head = Turtle("square")  # Create a square turtle object
            head.color("white")  # Set the color of the snake segments
            head.penup()  # Lift the pen to prevent drawing lines when moving
            head.goto(-20 * i, 0)  # Set the initial position of each segment
            self.body_snake.append(head)  # Add the segment to the snake's body

    def update_snake(self):
        # Add a new segment to the snake's body
        body = Turtle("square")  # Create a square turtle object
        body.color("white")  # Set the color of the new segment
        body.penup()  # Lift the pen to prevent drawing lines when moving
        body.goto(self.body_snake[-1].position())  # Set the position of the new segment
        self.body_snake.append(body)  # Add the segment to the snake's body

    def move_snake(self):
        # Move the snake forward
        for i in range(len(self.body_snake) - 1, 0, -1):
            new_x = self.body_snake[i-1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.body_snake[i-1].ycor()  # Get the y-coordinate of the previous segment
            self.body_snake[i].goto(new_x, new_y)  # Move the current segment to the position of the previous segment
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward

    def reset(self):
        # Reset the snake's position and length
        for part in self.body_snake:
            part.goto(1000, 1000)  # Move each segment off-screen
        self.body_snake.clear()  # Clear the list of snake segments
        self.create_snake()  # Recreate the initial segments of the snake
        self.head = self.body_snake[0]  # Set the head of the snake

    # Methods to change the direction of the snake
    def up(self):
        if self.head.heading() == DOWN:
            print("Invalid heading")  # Prevent the snake from moving in the opposite direction
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            print("Invalid heading")  # Prevent the snake from moving in the opposite direction
        else:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() == LEFT:
            print("Invalid heading")  # Prevent the snake from moving in the opposite direction
        else:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() == RIGHT:
            print("Invalid heading")  # Prevent the snake from moving in the opposite direction
        else:
            self.head.setheading(LEFT)
