from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        # Initialize the food object
        super().__init__()
        # Set the shape, color, size, and speed of the food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Refresh the food's position
        self.refresh()

    def refresh(self):
        # Generate random coordinates within the screen boundaries
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        # Move the food to the new random position
        self.goto(rand_x, rand_y)
