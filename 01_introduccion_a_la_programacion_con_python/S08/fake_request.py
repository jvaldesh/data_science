import requests
import json

def request(method, url, payload = ""):
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request(method, url, data = payload, headers = headers)
    if method in ["GET", "POST", "PUT"]:
        return json.loads(response.text)
    else:
        return response

list_users = "https://reqres.in/api/users"
desafio2 = request("GET", list_users)
print(desafio2)

create_user = "https://reqres.in/api/users"
user = {"name": "Julio", "job": "developer"}
desafio3 = request("POST", create_user, user)
print(desafio3)

update_user = "https://reqres.in/api/users/{}".format(desafio3["id"])
user = {"name": "Julio", "job": "devops"}
desafio4 = request("PUT", update_user, user)
print(desafio4)

delete_user = "https://reqres.in/api/users/{}".format(desafio3["id"])
desafio5 = request("DELETE", delete_user)
print(desafio5)