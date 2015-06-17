from application import app

@app.route('/', methods=["GET"])
def index():
    return 'Titles API'

@app.route('/validate/<titlenumber>', methods=["GET"])
def validateTitle(titlenumber):
    if titlenumber:
        return "Valid title"
    else:
        return "Invalid title"
