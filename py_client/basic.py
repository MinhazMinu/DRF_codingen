import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

get_response = requests.post(
    endpoint,
    params={"id": 456},
    json={"title": "Test tile", "content": "Test content", "price": 123.45},
)
print(get_response.status_code)
print(get_response.json())
