"""
Main function of generate submodule
"""

import os
import shutil
import sys

THIS_DIR, THIS_FILENAME = os.path.split(__file__)

def generate(dir):
    if os.path.exists(dir):
        print("ERROR: '{}' exists".format(dir))
        exit(1)
    os.makedirs(dir)
    tdir = os.path.join(THIS_DIR, 'templates')

    shutil.copy(tdir+'/plan.ev.tmpl', dir+'/plan.ev')
    for folder in ['people', 'rooms', 'talks']:
        os.makedirs(dir+'/'+folder)
    shutil.copy(tdir+'/people/abel.ppl.tmpl', dir+'/people/abel.ppl')
    shutil.copy(tdir+'/rooms/ex101.rm.tmpl', dir+'/rooms/ex101.rm')
    shutil.copy(tdir+'/talks/evplan.tk.tmpl', dir+'/talks/evplan.tk')
