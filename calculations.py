import os
import random
from dateutil.rrule import *
from dateutil.parser import *
import datetime


def generate():
    gen = random.choice(os.listdir('/app/res/'))
    smeh = '/app/res/{}'.format(gen)
    return str(smeh)


def siren_countdown():
    datelist = list(rrule(MONTHLY, count=100, byweekday=WE(1), dtstart=parse("2019-05-01T11:59:59")))
    dt = datetime.datetime
    now = dt.now()
    for nextsiren in range(len(datelist)):
        while now < datelist[nextsiren]:
            count = datelist[nextsiren] - dt(year=now.year, month=now.month, day=now.day,
                                             hour=now.hour+1, minute=now.minute, second=now.second)
            return 'До сирены осталось: {}'.format(count+datetime.timedelta(0, 1))