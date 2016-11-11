from enum import Enum


class TaskStatus(Enum):
    new = 0
    voted = 1
    under_voting = 2


class Task:
    def __init__(self, visual_id, name, description, status=TaskStatus.new):
        self.visual_id = visual_id
        self.name = name
        self.description = description
        self.status = status


class TaskView(Task):
    def __init__(self, visual_id, name, description, status=TaskStatus.new):
        super().__init__(visual_id, name, description, status)

    def get_voted_class(self):
        if self.status is TaskStatus.voted:
            return "voted"
        else:
            return ""

    def get_classes(self):
        return "%s" % self.get_voted_class()


class Player:
    def __init__(self, id, name, role=None):
        self.id = id
        self.name = name
        self.role = role


class PlayerView(Player):
    def __init__(self, id, name, role=None, admin=False, current=False):
        super().__init__(id, name, role)
        self.admin = admin
        self.current = current

    def get_role_class(self):
        if self.role is not None:
            return "role_%s" % self.role
        else:
            return ""

    def get_admin_class(self):
        if self.admin:
            return "admin"
        else:
            return ""

    def get_current_class(self):
        if self.current:
            return "current"
        else:
            return ""

    def get_classes(self):
        return "%s %s %s" % (self.get_role_class(), self.get_admin_class(), self.get_current_class())


class Board:
    def __init__(self, name, url, roles, admin):
        self.name = name
        self.url = url
        self.roles = roles
        self.admin = admin
        self.tasks = []
        self.players = []
        self.active_task = None
