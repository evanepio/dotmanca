# The Official Dotman Website

The Official Website for Dotman Comics

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

[![CircleCI](https://circleci.com/gh/evanepio/dotmanca.svg?style=svg)](https://circleci.com/gh/evanepio/dotmanca)

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
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DJANGO_ADMIN_URL=
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=UseAGeneratedValueOrDontAsItsLocal
DJANGO_ALLOWED_HOSTS=.dotman.ca
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True
```

You can review those settings, or accept as-is since this is for local. Do not use the above for production or UA environments. The `DATA_BASE_URL` must contain `POSTGRES_PASSWORD` and `POSTGRES_USER`.

Next, we can bring up the junk database to use:

    $ docker compose up -d

This only brings up a database. In the future, I'd probably want to bring up the `python managa.py runserver` with it as well.

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

```
poetry shell
export DJANGO_READ_DOT_ENV_FILE=True
export DJANGO_SETTINGS_MODULE=config.settings.test
coverage run manage.py test
coverage html
open htmlcov/index.html
```

#### Running tests with pytest

    $ pytest

> Note: you need `DJANGO_READ_DOT_ENV_FILE` set to `True` and `DJANGO_SETTINGS_MODULE` set to `config.settings.test` for it to work.

## Using VS Code Dev Container

1. Install Remote Containers Extension
2. Open the `dotmanca` project
3. Since I've committed `.devcontainer` directory, it should start the container immediately. If it says Docker is not installed and you know it is, click "Retry" and it should be good to go.
4. Open a terminal and enter `poetry install`, and everything should install properly.
5. Then run `poetry run which python` and set the python interpretter of VS Code to that value (this creates a `.vscode/settings.json` file in the project)

Your `.env` files should look like:

```
DJANGO_READ_DOT_ENV_FILE=True

POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_ADMIN_URL=
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=fantastic
DJANGO_ALLOWED_HOSTS=.dotman.ca
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

USE_S3=False
```