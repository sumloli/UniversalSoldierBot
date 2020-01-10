from bot import bot
from messages import *
from calculations import *
from db import *
import config
import apiai
import json


@bot.message_handler(commands=['c'])
def command(message):
    print(message)
    bot.send_message(message.chat.id, 'Your command is:')
    bot.send_message(message.chat.id, message.text[3:])
    bot.send_message(message.chat.id, 'Result:')


@bot.message_handler(commands=['lolstart'])
def send_welcome(message):
    bot.reply_to(message, HELLO_MESSAGE)


@bot.message_handler(commands=['lolhelp'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGE)


@bot.message_handler(commands=['siren'])
def send_siren(message):
    bot.reply_to(message, siren_countdown())


@bot.message_handler(commands=['db'])
def send_db(message):
    bot.reply_to(message, db())


@bot.message_handler(commands=['смех'])
def command_smeh(message):
    _ = generate()
    # print(_)
    if _ == '/app/res/igrivij.ogg':
        msg = 'Сегодня я игривый:'
    elif _ == '/app/res/impozantnij.ogg':
        msg = 'Сегодня я импозантный:'
    elif _ == '/app/res/iskrennij.ogg':
        msg = 'Сегодня я искренний:'
    elif _ == '/app/res/skromnij.ogg':
        msg = 'Сегодня я скромный:'
    elif _ == '/app/res/zagadochnij.ogg':
        msg = 'Сегодня я загадочный:'
    else:
        msg = 'Сегодня я САМОЗВАНЕЦ:'

    voice = open(_, 'rb')
    bot.send_message(message.chat.id, msg)
    bot.send_voice(message.chat.id, voice)


@bot.message_handler(regexp='(ору|лол|смешно|хах|хаха|азаз)')
def smeh(message):
    _ = generate()
    # print(_)
    if _ == '/app/res/igrivij.ogg':
        msg = 'Сегодня я игривый:'
    elif _ == '/app/res/impozantnij.ogg':
        msg = 'Сегодня я импозантный:'
    elif _ == '/app/res/iskrennij.ogg':
        msg = 'Сегодня я искренний:'
    elif _ == '/app/res/skromnij.ogg':
        msg = 'Сегодня я скромный:'
    elif _ == '/app/res/zagadochnij.ogg':
        msg = 'Сегодня я загадочный:'
    else:
        msg = 'Сегодня я САМОЗВАНЕЦ:'

    voice = open(_, 'rb')
    bot.send_message(message.chat.id, msg)
    bot.send_voice(message.chat.id, voice)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def text_message(message):
    print(message)
    if message.chat.type == "private" or (
            message.reply_to_message is not None and message.reply_to_message.from_user.id == 805621916) or (
            'entities' in message.json and message.json['entities'][0]['type'] == 'mention'):
        request = apiai.ApiAI(config.DF_TOKEN).text_request()
        request.lang = config.BOT_LANG
        request.session_id = config.DF_SESSION
        request.query = message.text
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']
        if response:
            bot.send_message(message.chat.id, text=response)
        else:
            bot.send_message(message.chat.id, text='Прости, но я тебя не понимаю(')


if __name__ == '__main__':
    bot.polling(none_stop=True)
