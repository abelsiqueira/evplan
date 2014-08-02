"""
This contains the demo for evplan
"""

import os
import random

def create_demo():
    """
    This will automatically generate a demo with random people, rooms and talks
    """
    dir="tmp.evplan.demo"
    if os.path.exists(dir):
        print("ERROR: '{}' exists".format(dir))
        exit(1)
    os.makedirs(dir)
    os.makedirs(dir+'/people')
    os.makedirs(dir+'/rooms')
    os.makedirs(dir+'/talks')

    create_demo_evplan(dir)
    people = create_demo_people(dir)
    create_demo_rooms(dir)
    create_demo_talks(dir,people)

def create_demo_evplan(dir):
    strout = "name: Demo Conference for evplan\n"
    strout += "location: Demoland\n"
    strout += "duration: 1900/12/13-1901/01/01,1901/01/04\n"
    strout += "times: 9h-12h,14h-17h\n"
    strout += "interval: 30\n"
    strout += "date_format: \"%B, %d of %Y\"\n"
    strout += "time_format: \"%Hh%M\"\n"
    with open(dir+'/plan.ev','w') as file:
        file.write(strout)

def create_demo_people(dir):
    people = ['name{:>03}'.format(i) for i in range(1,121)]
    for person in people:
        strout = "name: Demo Name {}\n".format(person);
        strout += "email: {}@fakemail.com\n".format(person);
        with open(dir+'/people/'+person+'.ppl','w') as file:
            file.write(strout)
    return people

def create_demo_rooms(dir):
    with open(dir+'/rooms/ex101.rm','w') as file:
        file.write("group: A\n")
    with open(dir+'/rooms/ex102.rm','w') as file:
        file.write("group: A\n")
    with open(dir+'/rooms/ex201.rm','w') as file:
        file.write("group: B\n")

def create_demo_talks(dir,people):
    tags = ['tag{:>02}'.format(i) for i in range(1,50)]
    for i in range(1,101):
        strout = "title: Demo Talk {}\n".format(i)
        if random.random() < 0.9:
            spks = people[random.randrange(0,len(people))]
        else:
            spks = ','.join([people[random.randrange(0,len(people))] \
                    for i in range(0,random.randint(2,5))])
        strout += "speakers: {}\n".format(spks)
        tgs = ','.join([tags[random.randrange(0,len(tags))] \
                for i in range(0,random.randint(3,6))])
        strout += "tags: {}\n".format(tgs)
        strout += "abstract: No abstract, this is a demo\n"
        with open('{}/talks/talk{:>03}.tk'.format(dir,i),'w') as file:
            file.write(strout)
