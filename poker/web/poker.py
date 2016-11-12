from flask import Flask, request, render_template, session, redirect, url_for

from model.model import Board, Player
from web import session_manager
from web.static_data_provider import ROLES, get_role_by_short_name, ESTIMATES
from web.utils import generate_id
from web.webapp import BasicWebApp
from web.webapp import GET, POST, GET_AND_POST


class Poker(BasicWebApp):
    def __init__(self, app: Flask):
        super().__init__(app, False)
        self.app.before_request(self.set_id)

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
            tasks = session_manager.get_tasks_to_display(id)
            players = session_manager.get_players_to_display(id, session['id'])
            board = session_manager.get_board(id)
            return render_template("board.html", tasks=tasks, players=players, board=board, estimates=ESTIMATES)
        else:
            return redirect(url_for("join_board", id=id))

    def debug_boards(self):
        return self.json_response(session_manager.BOARDS.keys())

    def get_mappings(self):
        return [
            ("/", GET, self.home),
            ("/board/new", POST, self.new_board),
            ("/board/<id>/join", GET_AND_POST, self.join_board),
            ("/board/<id>/join_as", POST, self.add_player_to_board),
            ("/board/<id>", GET, self.open_board)
        ]

    def get_debug_mappings(self):
        return [
            ("/debug/boards", GET, self.debug_boards)
        ]

    def set_id(self):
        if 'id' not in session:
            session['id'] = generate_id(25)
