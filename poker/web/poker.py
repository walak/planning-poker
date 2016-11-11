import random
import string

import collections
from flask import Flask, Request, Response, request, render_template, session, redirect, url_for

from model.model import Board, Player, Role
from web.utils import generate_id
import os
from web import session_manager
from jsonpickle import pickler
from web.static_data_provider import ROLES, get_role_by_short_name


class Poker:
    def __init__(self, app: Flask):
        self.app = app
        self.app.before_request(self.__set_id)
        self.app.secret_key = generate_id(40)
        self.__config_mappings()

    def start(self):
        self.app.run(port=8080, threaded=True)

    def home(self):
        return render_template("index.html", roles=ROLES)

    def new_board(self):
        if request.method == "POST":
            name = request.form['name']
            role_set = "with" == request.form['role_set']
            if role_set:
                roles = [get_role_by_short_name(r) for r in request.form.getlist('role[]')]
            else:
                roles = []
            admin = session['id']
            board = Board(name, generate_id(), roles, admin)
            session_manager.add_board(board)
            return redirect(url_for("join_board", id=board.url))

    def join_board(self, id):
        board = session_manager.get_board(id)
        board_admin = board.admin
        current_user = session['id']
        as_admin = current_user == board_admin
        return render_template("join.html", board=board, as_admin=as_admin)

    def add_player_to_board(self, id):
        nick = request.form['nick']
        role = get_role_by_short_name(request.form.get('role'))
        player_id = session['id']
        session_manager.get_board(id).players.append(Player(player_id, nick, role))
        return redirect(url_for("open_board", id=id))

    def open_board(self, id):
        if session_manager.is_player_on_board(session['id'], id):
            tasks = session_manager.get_board(id).tasks
            players = session_manager.get_players_to_display(id, session['id'])
            return render_template("board.html", tasks=tasks, players=players)
        else:
            return redirect(url_for("join_board", id=id))

    def __config_mappings(self):
        self.add_mapping("/", "GET", self.home)
        self.add_mapping("/board/new/", "POST", self.new_board)
        self.add_mapping("/board/<id>/join", ["GET", "POST"], self.join_board)
        self.add_mapping("/board/<id>/join_as", "POST", self.add_player_to_board)
        self.add_mapping("/board/<id>", "GET", self.open_board)

    def add_mapping(self, url, method_or_methods, handler):
        if isinstance(method_or_methods, collections.Iterable) and not isinstance(method_or_methods, str):
            mthds = list(method_or_methods)
        else:
            mthds = [method_or_methods]
        self.app.add_url_rule(url, view_func=handler, methods=mthds)

    def __set_id(self):
        if 'id' not in session:
            session['id'] = generate_id(25)


app = Flask(__name__, None, None, None, "../html")


@app.route("/debug/boards/")
def debug_boards():
    return as_json(session_manager.BOARDS.keys())


def as_json(entity):
    payload = pickler.encode(entity)
    return Response(response=payload, status=200, mimetype="application/json")


if __name__ == "__main__":
    poker = Poker(app)

    poker.start()
