#!/bin/sh

set -e

python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate --noinput

uwsgi --socket :8000 --master --enable-threads --module mysite.wsgi