import json
import requests

def validate_title(title_number):
    response = requests.post('http://localhost:8888/TitlesAdapter/titles/' + title_number)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    else:
        data = response.json()

        if data.validation_result = 1:
            data.error_message == "Valid title number"
        elif data.validation_result = 2:
            data.error_message == "Title number does not exist"
        else:
            data.error_message == "Invalid title number"

    return data
