from turtle import Turtle  # Import the Turtle module for creating graphical elements

# Constants for text alignment and font
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the scoreboard
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.score = 0  # Initialize the current score to 0
        with open("data.txt") as f:
            cur_score = f.read() # Read the high score from a file
            self.high_score =int(cur_score)
        self.write_score()  # Display the initial score on the screen

    def write_score(self):
        self.pencolor("white")
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to prevent drawing lines when moving
        self.goto(-20, 270)
        # Clear the previous score display
        self.clear()
        # Construct the text to display the current score and high score
        arg = f"Score: {self.score}    High score: {self.high_score}"
        # Write the text on the screen
        self.write(arg, move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        # Increment the score by 1
        self.score += 1
        # Update the displayed score
        self.write_score()

    def game_over(self):
        # Display a game over message
        self.goto(0, 0)
        self.write("Game over!", move=False, align=ALIGNMENT, font=FONT)

    def reset_original(self):
        # Check if the current score exceeds the high score
        if self.score > self.high_score:
            # Update the high score
            self.high_score = self.score
            # Write the new high score to the file
            with open("data.txt", mode='w') as f:
                f.write(str(self.score))
        # Reset the current score to 0
        self.score = 0
        # Update the displayed score
        self.write_score()
