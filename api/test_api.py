import requests
import json

# Sample data (replace with actual values)
sample_data = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}

# Send request to the API
response = requests.post(
    "http://localhost:5000/predict",
    headers={"Content-Type": "application/json"},
    data=json.dumps(sample_data)
)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")