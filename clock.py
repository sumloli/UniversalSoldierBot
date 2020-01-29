from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from calculations import *
import random

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def timed_job():
#     bot.send_message(-294448452, text='This job is run every minute.')
#     bot.send_message(-294448452, text='Test rounding of timestamp now:')
#     bot.send_message(-294448452, sirenCountdown().split(',')[0])
#     print('This job is run every minute.')


@sched.scheduled_job('cron', day='*', hour=11)
def scheduled_job():
    bot.send_message(-294448452, siren_countdown().split(',')[0])
    print('This job is run every day at 12.')


@sched.scheduled_job('cron', day='*', hour=10, minute=45)
def scheduled_job():
    bot.send_message(-294448452, f'Ежедневное напоминание что Саня - {random.choice(["красавчик", "пидор"])}')
    print('This job is run every day at 11.')


sched.start()
