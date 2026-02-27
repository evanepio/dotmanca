# The Official Dotman Website

The Official Website for Dotman Comics

[![CI CD](https://github.com/evanepio/dotmanca/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/evanepio/dotmanca/actions/workflows/ci-cd.yml)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

## Tech Stack

- **Python 3.14** / **Django**
- **PostgreSQL** — primary database
- **S3-compatible storage** (RustFS / MinIO) — static and media files
- **`uv`** — dependency and virtual environment management
- **`ruff`** — linting

## Quick Start (Dev Container)

I'm using Dev Containers so that everything starts up nice and proper. Just need VS Code and the Dev Containers extension.

After the container starts, run the following once to prepare the database and publish static assets:

```sh
uv run manage.py migrate
uv run manage.py collectstatic
```

> **Note:** Authorize `claude` from outside the Dev Container before starting, as it can't authorize reliably from inside. Make sure both `~/.claude` and `~/.claude.json` are mounted to the `vscode` user's home directory in the Dev Container.

## Basic Commands

### Running the dev server

```sh
uv run manage.py migrate
uv run manage.py runserver
```

> Note: `migrate` only needs to run once, but it's safe to run again — it detects no new migrations and does nothing.

### Creating a superuser

```sh
uv run manage.py createsuperuser
```

### Running tests

```sh
uv run pytest
```

> Note: `pyproject.toml` has configurations for `pytest` to work.

### Linting

```sh
uvx ruff check --diff .
```

### Formatting

This will check the formatting and report any errors:

```sh
uvx ruff format --check .
```

This will automatically format the code:

```sh
uvx ruff format
```

## Manual Setup (without Dev Containers)

> Keeping this section as a fallback in case of Dev Container issues.

You'll need:

- [Homebrew](https://brew.sh/)
- [Docker](https://www.docker.com/get-docker) or [OrbStack](https://orbstack.dev)

Install `uv`:

```sh
brew install uv
```

[Astral's](https://astral.sh) `uv` manages Python projects, dependencies, and virtual environments.

### Environment configuration

Copy `env.example` to `.env` and review the values:

```sh
cp env.example .env
```

> Do not use the example values for production or UA environments.

### Starting the backing services

Bring up the database and S3-compatible storage server:

```sh
docker compose up postgres -d
docker compose up s3 -d
```

> **Note:** You will need to manually create the bucket in MinIO (the S3-compatible server) after it starts.
