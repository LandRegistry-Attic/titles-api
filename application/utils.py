import json
import requests

def validate_title(title_number):
    response = requests.post('http://localhost:8889/titles/' + title_number)
    data = response.json()

    return data
