#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate --run-syncdb
python manage.py makemessages --all

uwsgi --socket :8000 --master --enable-threads --module app.wsgi