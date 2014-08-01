"""
These are related to the event
"""

import datetime
import os
import re
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
        self.read_people()
        self.read_rooms()
        self.read_talks()
        self.create_schedule()

    def read_plan(self):
        data = yaml.load(open('plan.ev'))
        self.name = data['name']
        self.location = data['location']
        self.duration = data['duration']
        self.times = data['times']
        self.interval = datetime.timedelta(minutes=int(data['interval']))
        self.date_format = data['date_format']
        self.time_format = data['time_format']
        days = []
        p1day = datetime.timedelta(days=1)
        for date in self.duration.split(','):
            date = date.split('-')
            if len(date) == 1:
                date = to_date(date[0])
                days.append(self.format_date(date))
            elif len(date) == 2:
                date[0] = to_date(date[0])
                date[1] = to_date(date[1])
                if date[0] >= date[1]:
                    print("ERROR: Badly formated date")
                while (date[0] <= date[1]):
                    days.append(self.format_date(date[0]))
                    date[0] += p1day
        times = []
        for pair in self.times.split(','):
            pair = pair.split('-')
            pair[0] = to_time(pair[0])
            pair[1] = to_time(pair[1])
            while pair[0] < pair[1]:
                times.append(self.format_time(pair[0]))
                pair[0] = pair[0] + self.interval
            if pair[0] > pair[1]:
                print("ERROR: Time interval not consistent with schedule")
                exit(1)
        self.days = days
        self.times = times

    def create_schedule(self):
        self.schedule = dict([(day, dict([(room, dict([(time,'') \
                for time in self.times])) for room in self.rooms])) \
                for day in self.days])

    def format_date(self, s):
        return s.strftime(self.date_format)

    def format_time(self, s):
        return s.strftime(self.time_format)

    def read_people(self):
        self.people = {}
        for dirname, dirnames, filenames in os.walk('people'):
            for person in filenames:
                p = yaml.load(open('people/'+person))
                id = os.path.splitext(person)[0]
                self.people[id] = p

    def read_rooms(self):
        self.rooms = {}
        for dirname, dirnames, filenames in os.walk('rooms'):
            for room in filenames:
                p = yaml.load(open('rooms/'+room))
                id = os.path.splitext(room)[0]
                self.rooms[id] = p

    def read_talks(self):
        self.talks = {}
        for dirname, dirnames, filenames in os.walk('talks'):
            for talk in filenames:
                p = yaml.load(open('talks/'+talk))
                p['tags'] = re.split('[,; ]', p['tags'])
                id = os.path.splitext(talk)[0]
                self.talks[id] = p

def to_time(s):
    v = re.split('[h:]', s)
    if len(v) == 1:
        return datetime.datetime(2000,1,1,int(v[0]))
    elif len(v) == 2:
        return datetime.datetime(2000,1,1,int(v[0]), int(v[1]))
    else:
        print("ERROR: Badly formatted time '{}'".format(s))
        exit(1)

def to_date(s):
    v = s.split('/')
    if len(v) != 3:
        print("ERROR: Badly formatted date '{}'".format(s))
        exit(1)
    return datetime.date(int(v[0]),int(v[1]),int(v[2]))

