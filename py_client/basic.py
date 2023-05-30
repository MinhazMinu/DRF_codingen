import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint, params={"id": 456}, json={"id": 123})
print(get_response.status_code)
print(get_response.json())
