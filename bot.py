import telebot
import config

bot = telebot.TeleBot(config.TG_TOKEN)
print(bot.get_me())
