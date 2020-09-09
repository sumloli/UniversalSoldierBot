from apscheduler.schedulers.blocking import BlockingScheduler
from bot import bot
from calculations import *
from db import *

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def timed_job():
#     bot.send_message(-266154989, text='This job is run every minute')
#     bot.send_message(-266154989, text='Test db_sanya func:')
#     bot.send_message(-266154989, f'Ежедневное напоминание что Саня - {db_sanya()}')
#     print('This job is run every minute.')



@sched.scheduled_job('interval', minutes=1)
def scheduled_job():
    bot.send_message(-294448452, text='DEBUG')
    bot.send_message(-294448452, text='This job is run every minute')
    bot.send_message(-294448452, siren_countdown().split(',')[0])
    print('This job is run every minute.')


@sched.scheduled_job('cron', day='*', hour=10)
def scheduled_job():
    bot.send_message(-294448452, siren_countdown().split(',')[0])
    print('This job is run every day at 12.')


@sched.scheduled_job('cron', day='*', hour=9)
def scheduled_job():
    bot.send_message(-294448452, f'Ежедневное напоминание что Саня - {db_sanya()}')
    print('This job is run every day at 11.')


sched.start()
