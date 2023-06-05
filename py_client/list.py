import requests

auth_response = requests.post(
    "http://127.0.0.1:8000/api/auth/",
    json={"username": "minhaz", "password": "1234"},
)

print(auth_response.status_code)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    endpoint = "http://127.0.0.1:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.status_code)
    print(get_response.json())
