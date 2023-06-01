import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {"title": "update Test tile", "price": 123.45}
get_response = requests.put(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())
