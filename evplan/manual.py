"""
Functions regarding the pdf manual
"""

import os
import re
import shutil

def create_manual(event):
    if not os.path.exists('_manual'):
        os.makedirs('_manual')
    if not os.path.exists('_manual/talks'):
        os.makedirs('_manual/talks')
    create_manual_tex(event)
    create_talks_tex(event)

def create_manual_tex(event):
    with open('templates/manual.tex.tmpl') as file:
        s = file.read()
    s = re.sub('TITLE', event.name, s)
    s = re.sub('VENUE', event.location, s)
    s = re.sub('DATE', ','.join(event.days), s)
    with open('_manual/manual.tex','w') as file:
        file.write(s)

def create_talks_tex(event):
    s = "\\chapter{Talks}\n"
    s += "\\newpage\n"
    sep = "\\begin{center}\n\\line(1,0){300}\\vspace{0.5cm}\\end{center}\n"
    s += sep.join(["\\input{talks/"+t+"}\n" for t in event.talks])
    with open('_manual/talks/talks.tex','w') as file:
        file.write(s)
    with open('templates/talk.tex.tmpl') as file:
        tmpl = file.read()
    for talk in event.talks:
        s = re.sub('TITLE', event.talks[talk]['title'], tmpl)
        s = re.sub('AUTHOR', event.talks[talk]['speakers'], s)
        s = re.sub('WHERE', event.talks[talk]['room'], s)
        when = event.talks[talk]['day'] + " - " + event.talks[talk]['time']
        s = re.sub('WHEN', when, s)
        s = re.sub('ABSTRACT', event.talks[talk]['abstract'], s)
        s = re.sub('TAGS', ','.join(event.talks[talk]['tags']), s)
        with open('_manual/talks/'+talk+'.tex','w') as file:
            file.write(s)
