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
