import json

from application import app
from .utils import validate_title

@app.route('/', methods=["GET"])
def index():
    return 'Titles API'

@app.route('/validate/<titlenumber>', methods=["GET"])
def validateTitle(titlenumber):
    request = validate_title(titlenumber)
    response = json.dumps(request)
    return response
