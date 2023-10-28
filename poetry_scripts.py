import os
import subprocess
import sys

from django.core.management import execute_from_command_line


def _execute(*sys_args):
    os.environ.setdefault("DJANGO_READ_DOT_ENV_FILE", "True")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    sys.argv = sys_args
    execute_from_command_line(sys.argv)


def run_server():
    """Run django build in server for local development"""
    _execute("manage.py", "runserver", "8080")


def run_lint():
    """Run `flake8` for linting"""
    result = subprocess.run("flake8")
    exit(result.returncode)


def run_check_format():
    """Run `black` to check if the code is pretty"""
    result = subprocess.run(["black", "--check", "--diff", "."])
    exit(result.returncode)


def run_auto_format():
    """Run `black` to make the code pretty"""
    result = subprocess.run(["black", "."])
    exit(result.returncode)


def run_sort_imports():
    """Run `isort` to sort imports"""
    result = subprocess.run(["isort", "--check", "--diff", "."])
    exit(result.returncode)


def manage():
    _execute("manage.py", *sys.argv[1:])
