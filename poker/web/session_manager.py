from model.model import PlayerView

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


def player_to_player_view(board, player, current_player):
    admin = player.id == board.admin
    current = player.id = current_player
    return PlayerView(player.id, player.name, player.role, admin, current)
