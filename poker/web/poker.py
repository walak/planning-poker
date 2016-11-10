import random
import string

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask.json import jsonify

from model.model import Board
from web.utils import generate_id
import os
from web import session_manager
from jsonpickle import pickler

boards = {}

app = Flask(__name__, None, None, None, "../html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/board/new/", methods=['POST'])
def new_board():
    if request.method == "POST":
        name = request.form['name']
        roles = request.form.getlist('role[]')
        board = Board(name, generate_id(), roles)
        session_manager.add_board(board)
        return as_json(board)


@app.route("/board/<id>/", methods=['GET'])
def open_board(id):
    board = session_manager.get_board(id)
    return render_template("join.html", name=board.name)


@app.route("/debug/boards/")
def debug_boards():
    return as_json(session_manager.BOARDS.keys())


def as_json(entity):
    payload = pickler.encode(entity)
    return Response(response=payload, status=200, mimetype="application/json")


if __name__ == "__main__":
    if os.environ.get('FLASK_DEBUG'):
        debug = os.environ['FLASK_DEBUG']
    else:
        debug = 0
    app.run(None, 8080, debug)
