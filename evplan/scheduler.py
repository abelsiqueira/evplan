"""
Here we have the functions that define the time of each talk.
"""

def scheduler(event):
    initial_schedule(event)
    update_talks(event)

def initial_schedule(event):
    day_i = 0
    room_i = 0
    time_i = 0
    day = event.days[day_i]
    rooms = list(event.rooms.keys())
    room = rooms[room_i]
    for talk in event.talks:
        time = event.times[time_i]
        event.schedule[day][room][time] = talk
        time_i += 1
        if (time_i == len(event.times)):
            time_i = 0
            room_i += 1
            if (room_i == len(event.rooms)):
                room_i = 0
                day_i += 1
                if (day_i == len(event.days)):
                    print("ERROR: Number of days is not enough for schedule")
                day = event.days[day_i]
            room = rooms[room_i]

def update_talks(event):
    for day in event.days:
        for time in event.times:
            for room in event.rooms:
                talk = event.schedule[day][room][time]
                if talk is not '':
                    event.talks[talk]['room'] = room
                    event.talks[talk]['time'] = time
                    event.talks[talk]['day'] = day

def raw_print(event):
    print(event.name)
    print('')
    for day in event.days:
        print(day)
        for time in event.times:
            for room in event.rooms:
                talk = event.schedule[day][room][time]
                if talk is not '':
                    print('{} - {}: {}'.format(time, room, talk))
