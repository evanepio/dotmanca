FROM mcr.microsoft.com/devcontainers/python:3.14

# Install Astral uv binaries from an already built image
COPY --from=astral/uv:0.11.16-python3.14-trixie /usr/local/bin/uv /usr/local/bin/uvx /bin/

USER vscode
