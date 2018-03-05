The Official Dotman Website
===========================

The Official Website for Dotman Comics

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

Getting Ready
-------------

This describes how I'll need to set up my dev environment in a mac (what I currently use ).

You'll need the following:

* [Homebrew](https://brew.sh/)
* [Docker](https://www.docker.com/get-docker)

Next run the following:

    $ brew install python3

This gives you a non-system, non version 2, python.

    $ pip3 install pipenv

The `pip3` will install in your `brew`-installed Python 3's `site-packages`. Just using `pip` will likely install in your system python, and that's not healthy.

Now from the root project directory:

    $ pipenv install

This will install all dependencies in the Pipfile. Also, it will create the virtual env to install those dependencies into.

To activate the new environment, use the following:

    $ pipenv shell

This will ensure the virtual env's python is first in your PATH. Just enter `exit` at the command prompt to go back to your regular shell (or close and reopen the terminal).

Settings
--------

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you\'ll see a \"Verify Your E-mail
    Address\" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user\'s email should be verified and ready to go.
-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
