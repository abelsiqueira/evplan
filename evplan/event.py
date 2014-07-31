"""
These are related to the event
"""

import datetime
import os
import yaml

PLAN_EV_FIELDS = ['name','location','duration','times','interval']

class Event(object):
    """
    The structure that holds all information of the event
    """
    def __init__(self):
        if (not os.path.exists('plan.ev') or not os.path.isdir('people') or
                not os.path.isdir('rooms') or not os.path.isdir('talks')):
            print("ERROR: run 'evplan generate' first")
            exit(1)

        self.read_plan()

    def read_plan(self):
        data = yaml.load(open('plan.ev'))
        self.name = data['name']
        self.location = data['location']
        self.duration = data['duration']
        self.times = data['times']
        self.interval = int(data['interval'])
        self.date_format = data['date_format']
        days = []
        p1day = datetime.timedelta(days=1)
        for date in self.duration.split(','):
            date = date.split('-')
            if len(date) == 1:
                date = to_date(date[0])
                days.append(date)
            elif len(date) == 2:
                date[0] = to_date(date[0])
                date[1] = to_date(date[1])
                if date[0] >= date[1]:
                    print("ERROR: Badly formated date")
                while (date[0] < date[1]):
                    days.append(date[0])
                    date[0] += p1day
        days = [self.format_date(day) for day in days]
        times = []
        for pair in self.times.split(','):
            a = time_str_to_int(pair.split('-')[0])
            b = time_str_to_int(pair.split('-')[1])
            while a < b:
                times.append(time_int_to_str(a))
                a += self.interval
            if a > b:
                print("ERROR: Time interval not consistent with schedule")
                exit(1)
        self.days = days;
        self.times = times;
        self.schedule = dict([(day, dict([(time,'') for time in times]))\
                for day in days])
        print(self.schedule)

    def format_date(self, s):
        return s.strftime(self.date_format)

def time_str_to_int(s):
    v = s.split('h')
    if len(v) == 1:
        return int(v[0])*60
    elif len(v) == 2:
        return int(v[0])*60 + int(v[1])
    else:
        print("ERROR: Wrong format for time: {}".format(s))
        exit(1)

def time_int_to_str(v):
    return '{}h{:0>2}'.format(int(v/60),v%60)

def to_date(s):
    v = s.split('/')
    return datetime.date(int(v[0]),int(v[1]),int(v[2]))

