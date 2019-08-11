# Server Setup

These are some basic instructions to set up a Linux server to run Gunicorn as a service.

## Install pyenv and Appropriate Python Version

To install `pyenv`, similar to `rbenv` for Ruby and `sdkman` for Java/Groovy, you might need the following dependencies:

    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

Once you've done that, use the [pyenv-installer](https://github.com/pyenv/pyenv-installer). After that, you shoulf be able to run:

    $ pyenv install 3.7.4

Of course replace 3.7.4 with the python version you want.

Then run either of the following commands:

    $ pyenv global 3.7.4
    $ pyenv local 3.7.4

Note that the difference is the `local` variant of the command will set the Python environment for the directory you run the command in.

## Install Poetry

Follow the instructions in the [Poetry docs](https://poetry.eustace.io/docs/).

## Check out Code and Create a Python Virtual Environment

Simple git clone, go into the project root and run:

    $ poetry install --no-dev

We pass the `--no-dev` flag to make sure we don't install a bunch of dev dependencies in our virtual environment.

## Settings

Create an `.env` file in the root of the project folder. It should contain the following items:

```
# General settings
# DJANGO_READ_DOT_ENV_FILE=True
DJANGO_ADMIN_URL=some_url_chunk
DJANGO_SETTINGS_MODULE=config.settings.production #use config.settings.test to use test-only settings
DJANGO_SECRET_KEY=USE A GENERATED VALUE
DJANGO_ALLOWED_HOSTS=.dotman.ca

# Security! Better to use DNS for this task, but you can use redirect
DJANGO_SECURE_SSL_REDIRECT=False

# Used to connect to the database. See Django docs for help.
DATABASE_URL="postgres://user:password@servername:5432/dbname"
```

Having this file allows the Django management commands to work. To allow `gunicorn` to have these settings, we'll need a different file in the systemd heirarchy:

## Gunicorn Settings

You'll need to create this `/etc/systemd/system/gunicorn.service` with the following contents:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=dotman
Group=www-data
WorkingDirectory=/path/to/root/dotmanca/project/writable/by/www-data
ExecStart=/path/to/virtual/env/where/dotmanca/and/gunicorn/installed/gunicorn --access-logfile - --workers 3 --bind unix:/some/path/to/sock/writable/by/www-data/dotmanca.sock config.wsgi

[Install]
WantedBy=multi-user.target
```

Since I don't know if Gunicorn can read `.env` files, we'll need `/etc/systemd/system/gunicorn.service.d/override.conf` with the following contents:

```
Environment="POSTGRES_PASSWORD=sameasEnvFile"
Environment="POSTGRES_USER=sameasEnvFile"
Environment="DJANGO_ADMIN_URL=sameasEnvFile"
Environment="DJANGO_SETTINGS_MODULE=config.settings.production"
Environment="DJANGO_SECRET_KEY=sameasEnvFile"
Environment="DJANGO_ALLOWED_HOSTS=.dotman.ca"
Environment="DJANGO_SECURE_SSL_REDIRECT=False"
Environment="DATABASE_URL=sameasEnvFile"
```

To restart:

```
sudo systemctl restart gunicorn
```

To check the status:

```
sudo systemctl status gunicorn
```

### NGINX Settings

Generally I want a `dotmanca` file in `/etc/nginx/sites-available` or wherever nginx is set up to read configurations from.

```
server {
    listen 80;
    server_name dotman.ca;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;

    ssl_certificate /path/of/cert/readable/by/www-data/cert.pem;
    ssl_certificate_key /path/of/key/readable/by/www-data/private_key.key;

    server_name dotman.ca;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /path/of/files/readable/by/www-data/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/some/path/to/sock/writable/by/www-data/dotmanca.sock;
    }
}
```

This basically sets up a secure site using a cert (from Let's Encrypt) and redirects any HTTP to HTTPS.

> Pay attention to the `proxy_pass` setting. It needs to match where you told gunicorn to write the socket file (Gunicorn's `--bind` option).

To restart:

```
sudo systemctl restart nginx
```

To check the status:

```
sudo systemctl status nginx
```

## CI / CD

To help with deploying automatically, we need to restart Gunicorn without a password prompt. We can do that by running the following:

    $ sudo visudo -f /etc/sudoers.d/dotman

I choose "dotman" so it sticks out, but any file name that doesn't end in `~` or contain a `.` will work. An editor will appear, and enter the follwoing:

```
%dotman ALL=NOPASSWD: /bin/systemctl restart gunicorn
```

This assumes `dotman` is the group your deploy user belongs to. Now you'll be able to run the following without a password prompt on next login:

    $ sudo /bin/systemctl restart gunicorn

Now you can allow your CI/CD system to log in with `ssh` using the public/private key thing, and it'll be able to run the command without being prompted for a password.

> Note: Starting the command with `sudo` is still required as is using the command as is in the `sudoers` file. For example, with the above file, `systemctl restart gunicorn` and `/bin/systemctl stop nginx` will not work.
