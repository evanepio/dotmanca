###############################################################################
# STAGE 1 - Build a common base to use for the remaining stages
###############################################################################
FROM python:3.12-slim@sha256:a64ac5be6928c6a94f00b16e09cdf3ba3edd44452d10ffa4516a58004873573e as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

###############################################################################
# STAGE 2 - Build the Virtual Environment with everything installed in it.
###############################################################################
FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.4.0 \
    DJANGO_DEBUG=False

COPY . .

RUN pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root && \
    poetry build && \
    ./.venv/bin/pip install dist/*.whl

###############################################################################
# STAGE 3 - Copy the virtual env from a previous stage to get final image
###############################################################################
FROM base as final

EXPOSE 8080

COPY --from=builder /app/.venv ./.venv
COPY docker-entrypoint.sh manage.py ./
RUN chmod u+x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]