import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "tejaswhinim132"
TOKEN = "qwertyuiop"
user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
today = datetime.now()
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?")
}

response = requests.post(url=pixel_creation_endpoint, json=post_data, headers=header)
print(response.text)
# update the graph
pixel_put_endpoint = f"{pixel_creation_endpoint}/20211127"
put_data = {
    "quantity": "35"
}
# response = requests.put(url=pixel_put_endpoint, json=put_data, headers=header)
# print(response.text)
# Delete the data
delete_pixel_endpoint = f"{pixel_creation_endpoint}/20211127"
# response = requests.delete(url=delete_pixel_endpoint, headers=header)
# print(response.text)