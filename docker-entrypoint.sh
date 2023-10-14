#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

postgres_ready() {
/app/.venv/bin/python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except psycopg2.OperationalError:
    print("Can not connect to database ${POSTGRES_DB} on ${POSTGRES_HOST} yet")
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

/app/.venv/bin/python manage.py migrate --no-input
/app/.venv/bin/python manage.py collectstatic --no-input
/app/.venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8080 --forwarded-allow-ips='*' config.wsgi:application
