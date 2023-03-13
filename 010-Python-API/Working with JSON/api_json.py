
import json

json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
data = json.loads(json_data)

print(data["name"])   # Output: John Doe
print(data["age"])    # Output: 30
print(data["city"])   # Output: New York


import requests

url = "https://api.example.com/data"
response = requests.get(url)

data = response.json()
print(data)
