import requests

# Define the endpoint and parameters
url = "https://api.census.gov/data/2020/dec/pl"
params = {
    "get": "NAME,P1_001N",
    "for": "state:*"
}

# Make the request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    for row in data:
        print(row)
else:
    print("Error:", response.status_code)
