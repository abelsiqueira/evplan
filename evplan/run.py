"""
Run is the command used in the working directory to generate the site and manual
of the event.
"""

from . import event
from . import scheduler
from . import manual
import os

def run():
    if (not os.path.exists('plan.ev') or not os.path.isdir('people') or
            not os.path.isdir('rooms') or not os.path.isdir('talks')):
        print("ERROR: run 'evplan generate' first")
        exit(1)
    ev = event.Event()
    scheduler.scheduler(ev)
    manual.create_manual(ev)
#    scheduler.raw_print(ev)
