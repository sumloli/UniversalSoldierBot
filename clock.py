from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from countdown import *

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    bot.send_message(-266154989, sirenCountdown())
    print('This job is run every minute.')


@sched.scheduled_job('cron', day='*', hour=18, minute=54)
def scheduled_job():
    bot.send_message(-266154989, sirenCountdown())
    print('This job is run every day at 12.')

sched.start()

