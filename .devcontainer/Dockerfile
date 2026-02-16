FROM mcr.microsoft.com/devcontainers/python:3.14

# Install Astral uv binaries from an already built image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

USER vscode