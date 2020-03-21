# STAGE 1 - Build a common base to use for the remaining stages
FROM python:3.8.1-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    DJANGO_DEBUG=False

WORKDIR /app

# STAGE 2 - Build the Virtual Enviuronemtn with everything installed in it.
FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.1

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl
RUN mv config /venv/lib/python3.8/site-packages/
RUN mv comics /venv/lib/python3.8/site-packages/
RUN mv gallery /venv/lib/python3.8/site-packages/
RUN mv characters /venv/lib/python3.8/site-packages/
RUN mv places /venv/lib/python3.8/site-packages/
RUN mv news /venv/lib/python3.8/site-packages/
RUN mv main /venv/lib/python3.8/site-packages/
RUN /venv/bin/python manage.py collectstatic --clear --no-input

# STAGE 3 - Copy final virtual environment to build a static assest image
FROM nginx:alpine as static-assests
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /venv/lib/python3.8/site-packages/staticfiles /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

# STAGE 4 - The final, built image - just copy the virtual env from a previous stage
FROM base as final

RUN apt-get update && apt-get install -y libpq-dev
COPY --from=builder /venv /venv
COPY docker-entrypoint.sh manage.py ./
RUN chmod u+x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]