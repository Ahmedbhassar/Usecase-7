import requests

url = 'https://lr-mode.onrender.com/predict'

data = {

    'highest_value': 20000000
}

response = requests.post(url, json=data)

print(response.json())