evplan - Event Planner
======================

WARNING: This does not work yet

This is a tool to help prepare an event in the line of conferences.
What I want from this tool is:

  - Generation of a schedule for all talks;
  - Use list of people per talk to prevent talk collision;
  - Use of tags to discourage same type of presentation in the same time;
  - Use of tags and room groups to put similar presentations together;
  - Creation of a site with all information;
  - Ability to work from windows and linux;
  - Possibility of integration with a GUI;
  - Creation of printed guides with schedule and additional information (I'm
    calling this manual).

License
=======

This work is under GPLv3 license, but you can use this to plan a closed event. I
only request that you mention this tool was used, including the link to the
github repository.

Install
=======

You will need Python 3. See the list of required packages in REQUIREMENTS.

How to use
==========

First, create your project using

    $ evplan generate NAME

Inside the folder will be a tree, like

  - plan.ev
  - speaker
  - rooms
  - talks
  - templates

The file `plan.ev` includes important details of the event, such as the name,
location and duration.
Inside `people`, there will be an example of a person.
Inside `rooms`, there will be an example of a room.
Inside `talks`, there will be an example file of a plenary talk.
Inside `templates`, there will templates for the manual tex files, and possibly
other templates.

Run

    $ evplan run

inside this folder to generate a `_site` folder with the site of the event (not
implemented yet), and a `_manual` folder with the pdfs of the event (only the
tex for now. Compile manual.tex).

For an example of event, run

    $ evplan demo
