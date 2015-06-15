import json

from application import app
from .utils import get_reference

from flask import request, Response

@app.route('/', methods=["GET"])
def index():
    return 'Title API'
