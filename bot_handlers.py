from bot import bot
from messages import *
from countdown import *
import os
import random

def generate():
    gen = random.choice(os.listdir('/app/res/'))
    smeh = '/app/res/{}'.format(gen)
    return str(smeh)
print(generate())

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

    voice = open(generate(), 'rb')
    bot.send_message(message.chat.id, msg)
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(regexp='(ору|лол|смешно|хах|хаха)')
def smeh(message):
    _ = generate()

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

    voice = open(generate(), 'rb')
    bot.send_message(message.chat.id, msg)
    bot.send_voice(message.chat.id, voice)


if __name__ == '__main__':
    bot.polling(none_stop=True)
