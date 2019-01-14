#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

export CACHE_TIMEOUT=100
export SECRET_KEY=FAKE_KEY
export DJANGO_SETTINGS_MODULE=mymdb.settings

cd $root/mymdb
python manage.py collectstatic
