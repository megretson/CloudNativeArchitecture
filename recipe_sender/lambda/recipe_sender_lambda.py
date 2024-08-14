import json
import requests

endpoint = "https://nx00qzo3ef.execute-api.us-east-2.amazonaws.com/prod2/recipes"

def lambda_handler(event, context):
    response = requests.post(endpoint, data=event)
    print(response.json())
