from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from countdown import *

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    @bot.message_handler(commands=['siren'])
    def send_help(message):
        bot.reply_to(message, sirenCountdown())
    print('This job is run every minute.')


#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
#def scheduled_job():
#    print('This job is run every weekday at 5pm.')

sched.start()

