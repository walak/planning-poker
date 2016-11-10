BOARDS = {}


def add_board(board):
    BOARDS[board.url] = board


def get_board(url):
    return BOARDS[url]
