from flask import Flask

from web.poker import Poker
from web.poker_api import PokerApi
from web.utils import generate_id

if __name__ == "__main__":
    app = Flask(__name__, template_folder="./html", static_folder="./static")
    app.secret_key = generate_id(40)
    app.url_map.strict_slashes = False

    poker = Poker(app)
    poker_api = PokerApi(app)

    app.run(port=8080, threaded=True)
