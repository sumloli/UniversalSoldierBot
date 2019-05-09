from bot import bot
from messages import *
from countdown import *
import os
import random

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
    bot.send_message(message.chat.id, 'доставлено:')
    voice = open(generate(), 'rb')
    #voice = open('/app/res/samozvanec.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(regexp='(ору|лол|смешно|хах|хаха)')
def smeh(message):
    voice = open(generate(), 'rb')
    bot.send_voice(message.chat.id, voice)


if __name__ == '__main__':
    bot.polling(none_stop=True)
