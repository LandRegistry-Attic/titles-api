from application import app

@app.route('/', methods=["GET"])
def index():
    return 'Title API'

@app.route('/validate/<titlenumber>', methods=["GET"])
def validateTitle(titlenumber):
    return true
