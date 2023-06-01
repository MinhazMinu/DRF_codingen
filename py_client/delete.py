import requests

pk_id = input("What is the id of the product you want to delete? ")

try:
    pk_id = int(pk_id)
except ValueError:
    pk_id = None
    raise ValueError("Please enter a valid integer")

if pk_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{pk_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code)
