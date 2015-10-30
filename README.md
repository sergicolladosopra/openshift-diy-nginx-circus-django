Python 3.5.0 + Nginx + Circus + Django on Openshift
==================================================

Running on local
================

requirements
------------
Install virtualenvwrapper [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) and [pip-tools](https://github.com/nvie/pip-tools),
create a virtualenv

    pip install virtualenvwrapper
    pip instal pip-tools
    mkvirtualenv envName
    workon envName

In order to automatically add  required environment vars install
[autoenv](https://github.com/kennethreitz/autoenv)

Install requirements:

    cd requirements
    pip-sync common.txt dev.txt

To add new requirements... add to requirements/common.in, then compile

    cd requirements
    pip compile common.in
    #if it's only needed in dev environment add to dev.in
    pip compile dev.in
    pip-sync common.txt dev.txt



Sync your db for the first time (In app folder )

    python manage.py migrate
    python manage.py

Create superUser:

    python manage.py createsuperuser

run:

    python manage.py runserver


Setting up Openshift
--------------------

Create the Openshift application with a DIY and Postgresql 8.4 cartridge (also works on MySQL and SQLite out-of-the-box):

    $ rhc app create <exampleapp> diy-0.1 postgresql-8.4
    $ cd <exampleapp>
    $ git remote add upstream -m master git:/github.com/sergicolladosopra/openshift-diy-nginx-circus-django.git
    $ git pull -s recursive -X theirs upstream master
    $ git push


Configuration
-------------
* Circus and Nginx configs are located in configs/ dir. Environments variables in this configs will substitute on deploy stage.
* If you want change the name of the Django project, please change it in the file .appname too.
* Django project is configured to work with PostgreSQL, MySQL or SQLite (in this priority order).
* Also this Django project will work on local machine: it will use SQLite, static and media folders will located in project folder.


Pre build stage
---------------

The 'pre_build' hook script performs the following actions:
* Installs Python 3.5.0
* Installs Virtualenv 1.9.1 and creates virtualenv in $OPENSHIFT_DATA_DIR/virtualenv
* Installs Nginx 1.4.0

You can install any version as you want, just change versions variables in this script


Build stage
-----------

* Installs a pip packages from 'requirements.txt' (Django>=1.5, psycopg2, uwsgi, Pillow)

Feel free to edit this file, but leave Circus and Django.


Deploy stage
------------

* Creates static and media dirs ($OPENSHIFT_DATA_DIR/static/static and $OPENSHIFT_DATA_DIR/static/media) for Django
* Substitute environments variables to Nginx and Circus configs and copy its to $OPENSHIFT_DATA_DIR


