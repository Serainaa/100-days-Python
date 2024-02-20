import requests
from datetime import datetime

USERNAME = "seraaaki"
TOKEN = "YDN+I715!giLcAN"
GRAPH_ID = "bicycle2ismygr"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
insert_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_graph_endpoint = f"{insert_graph_endpoint}/20230409"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 1. Create the user.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# Step 2. Create the graph.
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.today().strftime('%Y%m%d')

insert_params = {
    "date": today,
    "quantity": "6"
}

# Step 4. Insert data in the graph
# response = requests.post(url=insert_graph_endpoint, json=insert_params, headers=headers)
# print(response.status_code)

update_params = {
    "quantity": "3"
}

# Step 5. Update data.
response = requests.put(url=update_graph_endpoint, json=update_params, headers=headers)
print(response.status_code)

