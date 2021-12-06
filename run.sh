#!/bin/bash
if [ "$VIRTUAL_ENV" != "/home/hrobbin/python/django_car_app/env" ]
then
    . env/bin/activate
fi
python manage.py runserver localhost:8000