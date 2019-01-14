#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

cd $root
python manage.py collectstatic
