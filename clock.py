from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from countdown import *

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
#    bot.send_message(-294448452, text='This job is run every minute.')
#    bot.send_message(-294448452, sirenCountdown())
#    print('This job is run every minute.')


@sched.scheduled_job('cron', day='*', hour=11)
def scheduled_job():
    bot.send_message(-294448452, sirenCountdown())
    print('This job is run every day at 12.')


@sched.scheduled_job('cron', day='*', hour=10, minute=55)
def scheduled_job():
    bot.send_message(-294448452, '/pidor@SublimeBot')
    print('This job is run every day at 11.')

sched.start()
