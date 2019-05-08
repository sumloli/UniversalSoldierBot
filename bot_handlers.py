from bot import bot
from messages import *


@bot.message_handler(commands=['start', 'soldier'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)
    voice = open('/Users/sumloli/PycharmProjects/UniversalSoldierBot/res/smeh.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['help', 'start2'])
def send_welcome2(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(regexp='че по олдам')
def command_oldy(message):
    bot.send_message(message.chat.id, 'Сейчас проверим!')
    bot.send_message(message.chat.id, 'Олды тут?тест')


@bot.message_handler(regexp='(?:смех|смешно|лол)')
def command_oldy3(message):
    bot.reply_to(message.chat.id, 'ниже смех')
    voice = open('/app/res/smeh.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
