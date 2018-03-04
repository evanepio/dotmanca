The Official Dotman Website
===========================

The Official Website for Dotman Comics

[![Built with Cookiecutter Django]]

License

:   MIT

Settings
--------

Moved to [settings].

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

#### Running tests with py.test

    $ py.test

  [Built with Cookiecutter Django]: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
  [![Built with Cookiecutter Django]]: https://github.com/pydanny/cookiecutter-django/
  [settings]: http://cookiecutter-django.readthedocs.io/en/latest/settings.html