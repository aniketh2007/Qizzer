import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18",params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']





