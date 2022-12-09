###############################################################################
# STAGE 1 - Build a common base to use for the remaining stages
###############################################################################
FROM python:3.11-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

###############################################################################
# STAGE 2 - Build the Virtual Enviuronemtn with everything installed in it.
###############################################################################
FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.15 \
    DJANGO_DEBUG=False

RUN apt-get update && apt-get install -y libpq-dev &&\
    pip install "poetry==$POETRY_VERSION" &&\
    python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

###############################################################################
# STAGE 3 - Copy the virtual env from a previous stage to get final image
###############################################################################
FROM base as final

RUN apt-get update && apt-get install -y libpq-dev
COPY --from=builder /venv /venv
COPY docker-entrypoint.sh manage.py ./
RUN chmod u+x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]