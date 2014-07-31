"""
These are related to the event
"""

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
        t = int(data['interval'])
        self.schedule = []
        for pair in self.times.split(','):
            a = time_str_to_int(pair.split('-')[0])
            b = time_str_to_int(pair.split('-')[1])
            while a < b:
                self.schedule.append(time_int_to_str(a))
                a += t
            if a > b:
                print("ERROR: Time interval not consistent with schedule")
                exit(1)
        print(self.schedule)

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
