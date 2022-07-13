#!/bin/sh

set -e

python manage.py makemessages --all
python manage.py collectstatic --noinput
python manage.py migrate --run-syncdb

uwsgi --socket :8000 --master --enable-threads --module app.wsgi