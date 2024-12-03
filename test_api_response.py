import requests

BASE_URL = "http://127.0.0.1:5000"

# fetch all the jobs
try:
    response = requests.get(f"{BASE_URL}/jobs")
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as e:
    print(f"An error occurred: {e}")

# fetch all the jobs
try:
    response = requests.get(f"{BASE_URL}/jobs?status=In Progress")
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as e:
    print(f"An error occurred: {e}")



"""
# Create a customer
response = requests.post(f"{BASE_URL}/customers", json={
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "123-456-7890"
})
print(response.json())

# Create an engineer
response = requests.post(f"{BASE_URL}/engineers", json={
    "name": "Jane Smith",
    "designation": "Senior Engineer"
})
print(response.json())

# Create a complaint
response = requests.post(f"{BASE_URL}/complaints", json={
    "customer_id": 1,
    "category": "Internet Issue",
    "description": "Internet not working",
    "priority": "High"
})
print(response.json())

# Get all complaints
response = requests.get(f"{BASE_URL}/complaints/1")
print(response.json())
"""