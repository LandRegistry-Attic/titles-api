import json
import requests

def validate_title(title_number):
    response = requests.post('http://localhost:8888/TitlesAdapter/titles/' + title_number)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    else:
        data = response.json()

    return data
