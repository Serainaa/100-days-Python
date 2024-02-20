from turtle import Screen  # Import the Screen class for creating the game screen
import time  # Import the time module for controlling the game speed
from snake import Snake  # Import the Snake class for managing the snake
from food import Food  # Import the Food class for managing the food
from scoreboard import Scoreboard  # Import the Scoreboard class for displaying the score

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize the snake, food, and scoreboard
my_snake = Snake()
food = Food()
score = Scoreboard()
screen.update()  # Manually update the screen

# Listen for keyboard inputs
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause for a short time to control game speed
    my_snake.move_snake()  # Move the snake

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food's position
        my_snake.update_snake() # Extend the snake
        score.refresh()  # Refresh the score

    # Detect collision with wall
    x_cor = int(my_snake.head.xcor())
    y_cor = int(my_snake.head.ycor())
    if x_cor <= -290 or x_cor >= 290 or y_cor <= -290 or y_cor >= 290:
        score.reset()  # Reset the score
        my_snake.reset()  # Reset the snake
        score.reset_original() # Reser scoreboard

    # Detect collision with tail
    for segment in my_snake.body_snake[1:]:
        if my_snake.head.distance(segment) < 15:
            score.reset_original()  # Reset the score
            my_snake.reset()  # Reset the snake


# Exit the game when the screen is clicked
screen.exitonclick()
