import flask
from telebot import types
from config import *
from bot_handlers import bot
import os

server = flask.Flask(__name__)


@server.route('/' + TG_TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
        flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TG_TOKEN))
    return "Ну и че ты тут собирался увидеть, пидр?", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
