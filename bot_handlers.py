from bot import bot
from messages import *


@bot.message_handler(commands=['start', 'soldier'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)
    voice = open('/res/smeh.ogg', 'rb')
    bot.send_voice(chat_id, voice)
    bot.send_voice(chat_id, "FILEID")

@bot.message_handler(regexp='че по олдам')
def command_oldy(message):
    bot.send_message(message.chat.id, 'Сейчас проверим!')
    bot.send_message(message.chat.id, 'Олды тут?')


@bot.message_handler(regexp='че ')
def command_oldy3(message):
    bot.send_message(message.chat.id, 'Сейчас проверим!')
    bot.send_message(message.chat.id, 'Олды тут?')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
