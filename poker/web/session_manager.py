from model.model import PlayerView, TaskView

BOARDS = {}
PLAYERS = {}


def add_board(board):
    BOARDS[board.url] = board


def get_board(url):
    return BOARDS[url]


def add_new_player(player):
    PLAYERS[player.id] = player


def get_player(player_id):
    return PLAYERS[player_id]


def get_players_to_display(board_id, current_player):
    board = get_board(board_id)
    players = board.players
    return [player_to_player_view(board, p, current_player) for p in players]


def add_task_to_board(task, board_id):
    board = get_board(board_id)
    board.tasks.append(task)
    return get_tasks_to_display(board_id)


def get_tasks_to_display(board_id):
    board = get_board(board_id)
    return [TaskView.create_new(t) for t in board.tasks]


def player_to_player_view(board, player, current_player):
    admin = player.id == board.admin
    current = player.id == current_player
    return PlayerView(player.id, player.name, player.role, admin, current)


def is_player_on_board(player_id, board_id):
    return [p for p in BOARDS[board_id].players if p.id == player_id]
