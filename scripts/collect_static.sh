#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

export SECRET_KEY=FAKE_KEY
export DB_PASSWORD=FAKE_PASS
export SETTINGS_MODULE=mymdb.settings

cd $root
python manage.py collectstatic
