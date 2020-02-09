FROM python:3.8.1-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.1

RUN apt-get update && apt-get install -y libpq-dev
# RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
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

FROM base as final

RUN apt-get update && apt-get install -y libpq-dev
COPY --from=builder /venv /venv
COPY docker-entrypoint.sh manage.py ./
RUN chmod u+x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]