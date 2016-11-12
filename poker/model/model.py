from enum import Enum
from jsonpickle import pickler
import sys

from web.utils import generate_id


class TaskStatus(Enum):
    new = 0
    voted = 1
    under_voting = 2


class Task:
    def __init__(self, id, name, description, estimation, status=TaskStatus.new):
        self.id = id
        self.name = name
        self.description = description
        self.estimation = estimation
        self.status = status

    @staticmethod
    def create_new(name, description):
        return Task(generate_id(),
                    name,
                    description,
                    None,
                    TaskStatus.new)

    @staticmethod
    def from_json(json):
        return Task.create_new(json['name'], json['description'])

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return pickler.encode(self) == pickler.encode(other)


class TaskView(Task):
    def __init__(self, id, name, description, estimation, status=TaskStatus.new):
        super().__init__(id, name, description, estimation, status)

    @staticmethod
    def create_new(task):
        return TaskView(task.id, task.name, task.description, task.estimation, task.status)

    def get_voted_class(self):
        if self.status is TaskStatus.voted:
            return "voted"
        else:
            return ""

    def get_classes(self):
        return "%s" % self.get_voted_class()


class Role:
    def __init__(self, short_name, full_name, can_vote):
        self.short_name = short_name
        self.full_name = full_name
        self.can_vote = can_vote


class Estimate:
    def __init__(self, value, label):
        self.value = value
        self.label = label


class Estimation:
    pass


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
            return "role_%s" % self.role.short_name
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

    def with_roles(self):
        return len(self.roles) > 0
