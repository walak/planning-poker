from collections import Iterable

from flask import Flask
from flask import Response
from jsonpickle import pickler

GET = "GET"
POST = "POST"
GET_AND_POST = ["GET", "POST"]


class BasicWebApp:
    def __init__(self, app: Flask, debug_mode=False):
        self.app = app

        self.__add_mappings(self.get_mappings())
        if debug_mode:
            self.__add_mappings(self.get_debug_mappings())

    def get_mappings(self):
        return []

    def get_debug_mappings(self):
        return []

    def json_response(self, entity):
        payload = pickler.encode(entity)
        return Response(response=payload, status=200, mimetype="application/json")

    def __add_mappings(self, mpgs):
        [self.__add_mapping(m[0], m[1], m[2]) for m in mpgs]

    def __add_mapping(self, url, method_or_methods, handler):
        if isinstance(method_or_methods, Iterable) and not isinstance(method_or_methods, str):
            mthds = list(method_or_methods)
        else:
            mthds = [method_or_methods]
        self.app.add_url_rule(url, view_func=handler, methods=mthds)
