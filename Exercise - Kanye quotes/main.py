from tkinter import *
import requests

# Function to fetch Kanye West quote from API
def get_quote():
    # Send GET request to Kanye West quote API
    response = requests.get(url="https://api.kanye.rest/")
    
    # Check for any errors in the response
    response.raise_for_status()
    
    # Extract the quote message from the JSON response
    message = response.json()["quote"]
    
    # Update the displayed quote text on the canvas
    canvas.itemconfig(quote_text, text=message)

# Create main Tkinter window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas to display the background and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Load Kanye West image for button
kanye_img = PhotoImage(file="kanye.png")

# Create a button to fetch a new quote
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()
