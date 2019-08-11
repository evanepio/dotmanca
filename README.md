# The Official Dotman Website

The Official Website for Dotman Comics

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

[![Build Status](https://travis-ci.com/evanepio/dotmanca.svg?branch=master)](https://travis-ci.com/evanepio/dotmanca)

## Getting Ready

This describes how I'll need to set up my dev environment in a mac (what I currently use ).

You'll need the following:

- [Homebrew](https://brew.sh/)
- [Docker](https://www.docker.com/get-docker)

Next run the following:

    $ brew install pyenv

This gives you a way to manage multiple python versions at the same time.

> Note: `pyenv` is not the same as `virtualenv` or `venv`. Yay, naming!

Next, we need to install the correct Python version, and then switch to it.

    $ pyenv install 3.7.4
    $ pyenv global 3.7.4

If you just want the python version local to a particular directory, you can instead run the following inside the directory you want to run a specific version for:

    $ pyenv local 3.7.4

Next, we want to install Poetry. We can follow [these instructions](https://poetry.eustace.io/docs/).

Once Poetry is installed, we can run the following:

    $ poetry install

Create an `.env` file in the root of the project folder. It should contain the following items:

```
DJANGO_READ_DOT_ENV_FILE=True
POSTGRES_PASSWORD=django_pass
POSTGRES_USER=django_user
DJANGO_ADMIN_URL=
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=UseAGeneratedValueOrDontAsItsLocal
DJANGO_ALLOWED_HOSTS=.dotman.ca
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True
DATABASE_URL="postgres://django_user:django_pass@localhost:5432/django_user"
```

You can review those settings, or accept as-is since this is for local. Do not use the above for production or UA environments. The `DATA_BASE_URL` must contain `POSTGRES_PASSWORD` and `POSTGRES_USER`.

Next, we can bring up the junk database to use:

    $ docker-compose up -d

This only brings up a database. In the future, I'd probably want to bring up the `python managa.py runserver` with it as well.

## CI / CD

To help with deploying automatically, we need to restart Gunicorn without a password prompt. We can do that by running the following:

    $ sudo visudo -f /etc/sudoers.d/dotman

I choose "dotman" so it sticks out, but any file name that doesn't end in `~` or contain a `.` will work. An editor will appear, and enter the follwoing:

```
%dotman ALL=NOPASSWD: /bin/systemctl restart gunicorn
```

This assumes `dotman` is the group your deploy user belongs to. Now you'll be able to run the following without a password prompt on next login:

    $ sudo /bin/systemctl restart gunicorn

Now you can allow your CI/CD system to log in with `ssh` using the public/private key thing, and it'll be able to run the command without being prompted for a password.

> Note: Starting the command with `sudo` is still required as is using the command as is in the `sudoers` file. For example, with the above file, `systemctl restart gunicorn` and `/bin/systemctl stop nginx` will not work.

## Settings

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

## Basic Commands

### Running locally

```
poetry shell
export DJANGO_READ_DOT_ENV_FILE=True
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py runserver
```

### Setting Up Your Users

- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
