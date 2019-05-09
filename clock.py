from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from countdown import *

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    bot.send_message(-266154989, sirenCountdown())
    print('This job is run every minute.')


@sched.scheduled_job('cron', day='*', hour=18, minutes=50)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()

