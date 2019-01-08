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

Create an `.env` file in the root of the project folder. It should contain the following items:

```
# General settings
# DJANGO_READ_DOT_ENV_FILE=True
DJANGO_ADMIN_URL=some_url_chunk
DJANGO_SETTINGS_MODULE=config.settings.production #use config.settings.test to use test-only settings
DJANGO_SECRET_KEY=USE A GENERATED VALUE
DJANGO_ALLOWED_HOSTS=.dotman.ca

# Security! Better to use DNS for this task, but you can use redirect
DJANGO_SECURE_SSL_REDIRECT=False

# Used to connect to the database. See Django docs for help.
DATABASE_URL="postgres://user:password@servername:5432/dbname"
```

Having this file allows the Django management commands to work. To allow `gunicorn` to have these settings, we'll need a different file in the systemd heirarchy:

### Gunicorn Settings

You'll need to create this `/etc/systemd/system/gunicorn.service` with the following contents:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=dotman
Group=www-data
WorkingDirectory=/path/to/root/dotmanca/project/writable/by/www-data
ExecStart=/path/to/virtual/env/where/dotmanca/and/gunicorn/installed/gunicorn --access-logfile - --workers 3 --bind unix:/some/path/to/sock/writable/by/www-data/dotmanca.sock config.wsgi

[Install]
WantedBy=multi-user.target
```

Since I don't know if Gunicorn can read `.env` files, we'll need `/etc/systemd/system/gunicorn.service.d/override.conf` with the following contents:

```
Environment="POSTGRES_PASSWORD=sameasEnvFile"
Environment="POSTGRES_USER=sameasEnvFile"
Environment="DJANGO_ADMIN_URL=sameasEnvFile"
Environment="DJANGO_SETTINGS_MODULE=config.settings.production"
Environment="DJANGO_SECRET_KEY=sameasEnvFile"
Environment="DJANGO_ALLOWED_HOSTS=.dotman.ca"
Environment="DJANGO_SECURE_SSL_REDIRECT=False"
Environment="DATABASE_URL=sameasEnvFile"
```

To restart: 

```
sudo systemctl restart gunicorn
```

To check the status:

```
sudo systemctl status gunicorn
```

### NGINX Settings

Generally I want a `dotmanca` file in `/etc/nginx/sites-available` or wherever nginx is set up to read configurations from.

```
server {
    listen 80;
    server_name dotman.ca;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;

    ssl_certificate /path/of/cert/readable/by/www-data/cert.pem;
    ssl_certificate_key /path/of/key/readable/by/www-data/private_key.key;

    server_name dotman.ca;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /path/of/files/readable/by/www-data/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/some/path/to/sock/writable/by/www-data/dotmanca.sock;
    }
}
```

This basically sets up a secure site using a cert (from Let's Encrypt) and redirects any HTTP to HTTPS.

> Pay attention to the `proxy_pass` setting. It needs to match where you told gunicorn to write the socket file (Gunicorn's `--bind` option).

To restart: 

```
sudo systemctl restart nginx
```

To check the status:

```
sudo systemctl status nginx
```

Basic Commands
--------------

### Setting Up Your Users

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
