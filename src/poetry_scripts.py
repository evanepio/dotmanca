import os
import subprocess
import sys

from django.core.management import execute_from_command_line


def _django_execute(*sys_args):
    os.environ.setdefault("DJANGO_READ_DOT_ENV_FILE", "True")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    sys.argv = sys_args
    execute_from_command_line(sys.argv)


def run_server():
    """Run django build in server for local development"""
    _django_execute("manage.py", "runserver", "8080")


def manage():
    """Run Django Manage commands from `poetry run`"""
    _django_execute("manage.py", *sys.argv[1:])


def run_tests():
    """Run `pytest` to make sure some of the code runs"""
    result = subprocess.run(["pytest"])
    exit(result.returncode)


def run_coverage():
    """Run `pytest` to make sure some of the code runs"""
    subprocess.run(["coverage", "run", "-m", "pytest"])
    result = subprocess.run(["coverage", "html"])
    exit(result.returncode)


def run_lint():
    """Run `ruff` for linting"""
    result = subprocess.run(["ruff", "check", "."])
    exit(result.returncode)


def run_check_format():
    """Run `black` to check if the code is pretty"""
    result = subprocess.run(["ruff", "format", "--diff", "."])
    exit(result.returncode)


def run_auto_format():
    """Run `black` to make the code pretty"""
    result = subprocess.run(["ruff", "format", "."])
    exit(result.returncode)


def run_sort_imports():
    """Run `isort` to sort imports"""
    result = subprocess.run(["isort", "--check", "--diff", "."])
    exit(result.returncode)
