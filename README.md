evplan - Event Planner
======================

This is a tool to help prepare an event in the line of conferences.
What I want from this tool is:

  - Generation of a schedule for all talks;
  - Use list of participants per talk to prevent talk collision;
  - Use of tags to discourage same type of presentation in the same time;
  - Use of tags and room groups to put similar presentations together;
  - Creation of a site with all information;
  - Ability to work from windows and linux;
  - Possibility of integration with a GUI;
  - Creation of printed guides with schedule and additional information(manual?,
    how's this called?).

I think the easiest way to have this happen is using Python.

License
=======

This work is under GPLv3 license, but you can use this to plan a closed event. I
only request that you mention this tool was used, including the link to the
github repository.

Install
=======

You will need Python 3, git and pdflatex.

How to use
==========

WARNING: It will work like this, currently doesn't.

First, create your project using

    $ evclan create NAME

Inside the folder will be a tree, like

  - plan.ev
  - speaker
  - rooms
  - talks

along with some hidden files.
The file `plan.ev` includes important details of the event, such as the name,
location and duration.
Inside `participants`, there will be an example of a participant.
Inside `rooms`, there will be an example of a room.
Inside `talks`, there will be an example file of a plenary talk.

Run

    $ evclan run

inside this folder to generate a `_site` folder with the site of the event, and
a `_manual` folder with the pdfs of the event.
