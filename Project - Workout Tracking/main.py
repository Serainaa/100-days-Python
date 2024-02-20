import requests
from datetime import datetime
import os

# Define the endpoint for the natural language exercise
natural_language_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Retrieve API credentials from environment variables
API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_URL = os.environ["SHEETY_URL"]

# Prompt user to input exercises
query = input("Tell me which exercises you did:")

# Define headers for the POST request to Nutritionix API
headers = {
    "x-app-id": os.environ.get("API_ID"),
    "x-app-key": os.environ.get("API_KEY")
}

# Parameters for the request to Nutritionix API
my_parameters = {
    "query": query
}

# Headers for the request to Sheety API
bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
}

# Send request to Nutritionix API
response = requests.post(url=natural_language_exercise_endpoint, json=my_parameters, headers=headers)
response.raise_for_status()

# Extract exercise data from the response
exercises = response.json()["exercises"]
print(len(exercises))

# Loop through each exercise and send data to Sheety API
for exercise in exercises:
    # Prepare data parameters for Sheety API
    data_params = {
        "workout": {
            "date": datetime.today().strftime('%d/%m/%Y'),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    print(data_params)
    
    # Send POST request to Sheety API
    second_response = requests.post(url=os.environ.get('SHEETY_URL'), json=data_params, headers=bearer_headers)
    second_response.raise_for_status()
