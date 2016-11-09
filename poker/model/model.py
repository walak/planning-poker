class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Session:
    def __init__(self):
        self.tasks = []
        self.players = []

    def add_player_to_session(self, player):
        self.players.append(player)

    def add_task(self, task):
        self.tasks.append(task)

    def get_players(self):
        return [self.players]


class Voting:
    def __init__(self, task):
        self.task = task
        self.votes = []


class Vote:
    def __init__(self, player, value):
        self.player = player
        self.value = value


class Board:
    def __init__(self, name, url, roles):
        self.name = name
        self.url = url
        self.roles = roles
