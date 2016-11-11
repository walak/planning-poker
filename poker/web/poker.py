import random
import string

from flask import Flask, Request, Response, request, render_template, session, redirect, url_for

from model.model import Board, Player
from web.utils import generate_id
import os
from web import session_manager
from jsonpickle import pickler
from web.static_data_provider import ROLES

app = Flask(__name__, None, None, None, "../html")
app.secret_key = generate_id(40)


@app.before_request
def session_aware():
    if 'id' not in session:
        session['id'] = generate_id(25)


@app.route("/")
def home():
    return render_template("index.html", roles=ROLES)


@app.route("/board/new/", methods=['POST'])
def new_board():
    if request.method == "POST":
        name = request.form['name']
        roles = request.form.getlist('role[]')
        admin = session['id']
        board = Board(name, generate_id(), roles, admin)
        session_manager.add_board(board)
        return redirect(url_for("join_board", id=board.url))


@app.route("/board/<id>/join", methods=['GET', 'POST'])
def join_board(id):
    board = session_manager.get_board(id)
    board_admin = board.admin
    bid = board.url
    current_user = session['id']
    as_admin = current_user == board_admin
    return render_template("join.html", name=board.name, admin=as_admin, bid=bid)


@app.route("/board/<id>/join_as", methods=['POST'])
def add_player_to_board(id):
    nick = request.form['nick']
    role = request.form['role']
    player_id = session['id']
    session_manager.get_board(id).players.append(Player(id, nick))
    return redirect(url_for("open_board", id=id))


@app.route("/board/<id>", methods=['GET'])
def open_board(id):
    tasks = session_manager.get_board(id).tasks
    players = session_manager.get_players_to_display(id, session['id'])
    return render_template("board.html", tasks=tasks, players=players)


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
