import requests 

parameters = {
    "amount" : 20,
    "category" : 18,
    "type" : "boolean"
}
response = requests.get(url="https://opentdb.com/api.php?amount=20&category=18&type=boolean",params=parameters)
response.raise_for_status()
data= response.json()
question_data = data["results"]
