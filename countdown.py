from dateutil.rrule import *
from dateutil.parser import *
import datetime


def sirenCountdown():
    datelist = list(rrule(MONTHLY, count=10, byweekday=WE(1), dtstart=parse("2019-05-01T11:59:59")))
    dt = datetime.datetime
    now = dt.now()
    count = datelist[1] - dt(year=now.year, month=now.month, day=now.day,
                             hour=now.hour+2, minute=now.minute, second=now.second)

    return 'До сирены осталось: {}'.format(count)
