import requests

BASE_URL = "http://127.0.0.1:5000"

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
