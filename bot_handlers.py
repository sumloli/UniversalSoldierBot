from bot import bot
from messages import *
from countdown import *
import config
import os
import random
import apiai, json


def generate():
    gen = random.choice(os.listdir('/app/res/'))
    smeh = '/app/res/{}'.format(gen)
    return str(smeh)


@bot.message_handler(commands=['lolstart'])
def send_welcome(message):
    bot.reply_to(message, HELLO_MESSAGE)


@bot.message_handler(commands=['lolhelp'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGE)


@bot.message_handler(commands=['siren'])
def send_siren(message):
    bot.reply_to(message, sirenCountdown())


@bot.message_handler(commands=['смех'])
def command_smeh(message):
    _ = generate()
    print(_)
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
    print(_)
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
    if message.chat.type == "private" or message.chat.id == 805621916:
        request = apiai.ApiAI(config.DF_TOKEN).text_request()  # Token API of Dialogflow
        request.lang = config.BOT_LANG  # lang of request
        request.session_id = config.DF_SESSION  # ID of dialog session (for bot learning)
        request.query = message.text  # Send request to AI with user's message
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']  # Retrieve json and get the answer
        # If we take answer back, we will send it to the user, else we can't understand user
        if response:
            bot.send_message(message.chat.id, text=response)
        else:
            bot.send_message(message.chat.id, text='Прости, но я тебя не понимаю(')


if __name__ == '__main__':
    bot.polling(none_stop=True)
