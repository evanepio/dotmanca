# The Official Dotman Website

The Official Website for Dotman Comics

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

## Getting Ready

This describes how I'll need to set up my dev environment in a mac (what I currently use ).

You'll need the following:

- [Homebrew](https://brew.sh/)
- [Docker](https://www.docker.com/get-docker) or [OrbStack](https://orbstack.dev)

Next run the following:

    $ brew install uv

[Astral's](https://astral.sh) `uv` manages Python projects, dependencies and virtual environments.

Create an `.env` file in the root of the project folder. It should contain the following items:

```
DJANGO_READ_DOT_ENV_FILE=True
POSTGRES_PASSWORD=django_pass
POSTGRES_USER=django_user
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DJANGO_ADMIN_URL=admin
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=UseAGeneratedValueOrDontAsItsLocal
DJANGO_ALLOWED_HOSTS=.dotman.ca
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

USE_S3=True
AWS_S3_ENDPOINT_URL=http://localhost:9000
AWS_ACCESS_KEY_ID=minioadmin
AWS_SECRET_ACCESS_KEY=minioadmin
AWS_STORAGE_BUCKET_NAME=dotmanca
AWS_S3_REGION_NAME=
DOTMAN_STATIC_AND_MEDIA_BASE_URL=http://localhost:9000

STATIC_LOCATION=static
PUBLIC_MEDIA_LOCATION=media
```

You can review those settings, or accept as-is since this is for local. Do not use the above for production or UA environments.

Next, we can bring up the junk database to use:

    $ docker compose up postgres -d

And we'll also want a junk S3 server to use:

    $ docker compose up s3 -d

These commands only bring up a database and and S3 compatible server.

> Note: you will need to create the busket in Minio (the S3 compatible server) manually.

## Basic Commands

### Running locally

```
uv run --env-file .env manage.py migrate
uv run --env-file .env manage.py runserver
```
> Note: you only need to run the `migrate` once, but it never hurts to run again (it'll detect no new migrations, and do nothing).

### Setting Up Your Users

- To create an **superuser account**, use this command:

      $ uv run --env-file .env manage.py createsuperuser

#### Running tests with `pytest`

    $ uv run pytest

> Note: `pyproject.toml` has configurations for `pytest` to work.

### Lint code

This project uses `ruff` to lint code. We can run it with the following:

```
uv run ruff check --diff .
```
