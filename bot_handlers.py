from bot import bot
from messages import *


@bot.message_handler(regexp='Jsem Vojta')
def command_oldy7(message):
    bot.send_message(message.chat.id, 'Hello Vojto Glad to see you!')


@bot.message_handler(commands=['start', 'old', 'OldyGoRmkBot'])
def send_welcome(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(regexp='че по олдам')
def command_oldy(message):
    bot.send_message(message.chat.id, 'Сейчас проверим!')
    bot.send_message(message.chat.id, 'Олды тут?')


@bot.message_handler(regexp='OldyGoRmkBot')
def command_oldy1(message):
    bot.send_message(message.chat.id, 'Че надо?')


@bot.message_handler(regexp='на месте')
def command_oldy2(message):
    bot.send_message(message.chat.id, 'Олды на месте!')


@bot.message_handler(regexp='аниме')
def command_oldy3(message):
    bot.send_message(message.chat.id, 'Аниме говно!')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)