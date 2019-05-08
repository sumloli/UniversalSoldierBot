from bot import bot
from messages import *


#@bot.message_handler(commands=['start', 'soldier'])
#def send_welcome(message):
#    bot.send_message(message.chat.id, HELLO_MESSAGE)
#    voice = open('/app/res/smeh.ogg', 'rb')
#    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['lolstart'])
def send_welcome(message):
    bot.reply_to(message, HELLO_MESSAGE)

@bot.message_handler(commands=['lolhelp'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGE)

@bot.message_handler(commands=['смех'])
def command_smeh(message):
    bot.send_message(message.chat.id, 'доставлено:')
    voice = open('/app/res/smeh.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(regexp='(ору|лол|смешно|хах|хаха)')
def smeh(message):
    voice = open('/app/res/smeh.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

#@bot.message_handler(regexp='(?:смех|смешно)')
#def command_oldy3(message):
#    bot.send_message(message.chat.id, 'ниже смех')
#    voice = open('/app/res/smeh.ogg', 'rb')
#    bot.send_voice(message.chat.id, voice)

#@bot.message_handler(content_types=['text'])
#def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
