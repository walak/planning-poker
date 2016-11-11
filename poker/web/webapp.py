from collections import Iterable
from flask import Flask, session
from web.utils import generate_id


class BasicWebApp:
    MAPPINGS = []
    DEBUG_MAPPINGS = []

    def __init__(self, app: Flask, use_session_id=False, debug_mode=False):
        self.app = app
        if use_session_id:
            self.app.before_request(self.set_id)

        self.__add_mappings(self.MAPPINGS)
        if debug_mode:
            self.__add_mappings(self.DEBUG_MAPPINGS)

    def set_id(self):
        if 'id' not in session:
            session['id'] = generate_id(25)

    def __add_mappings(self, mpgs):
        [self.__add_mapping(m[0], m[1], m[3]) for m in mpgs]

    def __add_mapping(self, url, method_or_methods, handler):
        if isinstance(method_or_methods, Iterable) and not isinstance(method_or_methods, str):
            mthds = list(method_or_methods)
        else:
            mthds = [method_or_methods]
        self.app.add_url_rule(url, view_func=handler, methods=mthds)
