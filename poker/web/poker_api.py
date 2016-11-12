from flask import Flask
from flask import Request
from flask import Response
from flask import request
from flask import session

from model.model import Task
from web.webapp import BasicWebApp, GET, POST
from web import session_manager


class PokerApi(BasicWebApp):
    def __init__(self, app: Flask, debug_mode=False):
        super().__init__(app, debug_mode)

    def get_players_for_board(self, board_id):
        current_player = session['id']
        return self.json_response(session_manager.get_players_to_display(board_id, current_player))

    def get_tasks_for_board(self, board_id):
        return self.json_response(session_manager.get_tasks_to_display(board_id))

    def add_task_to_board(self, board_id):
        payload = request.get_json()
        task = Task.from_json(payload)
        tasks = session_manager.add_task_to_board(task, board_id)
        return self.json_response(tasks)

    def get_mappings(self):
        return [
            ("/board/<board_id>/players", GET, self.get_players_for_board),
            ("/board/<board_id>/tasks", GET, self.get_tasks_for_board),
            ("/board/<board_id>/tasks/add", POST, self.add_task_to_board)
        ]
