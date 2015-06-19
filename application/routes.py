from application import app

from .utils import validate_title

@app.route('/', methods=["GET"])
def index():
    return 'Titles API'

@app.route('/validate/<titlenumber>', methods=["GET"])
def validateTitle(titlenumber):
    return_code = validate_title(titlenumber)
    response = ""

    if return_code == "1":
        response = "Valid Title"
    elif return_code == "2":
        response = "Unknown Title"
    elif return_code == "3":
        response = "Invalid Title"
    else:
        response = "Title Validation Error"
