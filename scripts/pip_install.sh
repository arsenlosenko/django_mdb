#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

pip install --upgrade pip
pip3 install -r $root/requirements.prod.txt
