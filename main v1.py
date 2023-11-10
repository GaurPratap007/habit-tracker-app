# TODO: Make a GUI App: 1. Get input, 2. Show output, 3. Update graph

import requests
from datetime import datetime

TOKEN = ""
USERNAME = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#response = requests.post(url = pixela_endpoint, json= user_params)
#print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Reading Count",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers ={
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

# Add pixels in graph
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Update pixels
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=new_data, headers=headers)
# print(response.text)

# Delete Pixels
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
