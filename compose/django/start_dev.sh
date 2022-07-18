#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py auto_createsuperuser
python manage.py auto_createsocialapp
python manage.py runserver 0.0.0.0:8000
