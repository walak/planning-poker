import random
import string

from flask import Flask
from flask import request
from flask import render_template
from web.utils import generate_id
import os

boards = {}

app = Flask(__name__, None, None, None, "../html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/board/new/",methods=['POST'])
def new_board():
    if request.method == "POST":
        name = request.form['name']
        roles = request.form['role']


if __name__ == "__main__":
    if os.environ.get('FLASK_DEBUG'):
        debug = os.environ['FLASK_DEBUG']
    else:
        debug = 0
    app.run(None, 8080, debug)
