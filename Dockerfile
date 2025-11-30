# Lifted from https://github.com/astral-sh/uv-docker-example/blob/main/multistage.Dockerfile

#####################################
# Stage 1 - Build Virtual Environment
#####################################
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Disable Python downloads, because we want to use the system interpreter
# across both images. If using a managed Python version, it needs to be
# copied from the build image into the final image; see `standalone.Dockerfile`
# for an example.
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Need this stuff for CFFI, which is used by the password hasher argon2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY uv.lock /app/uv.lock
COPY pyproject.toml /app/pyproject.toml
RUN uv sync --locked --no-install-project --no-dev

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

############################################################
# Stage 2 - Copy Virtual Environment to a clean Python image
############################################################
FROM python:3.14-slim-bookworm
# It is important to use the image that matches the builder, as the path to the
# Python executable must be the same, e.g., using `python:3.11-slim-bookworm`

EXPOSE 8080/tcp

# Setup a non-root user
RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

# Copy the application from the builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Use `/app` as the working directory
WORKDIR /app

COPY docker-entrypoint.sh manage.py ./
RUN chmod u+x docker-entrypoint.sh

# Use the non-root user to run our application - after chmod
USER nonroot

CMD ["./docker-entrypoint.sh"]
