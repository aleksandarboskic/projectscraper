#!/bin/bash
python manage.py migrate 
python manage.py createsuperuserwithpassword --username $1 --password $2 --email $3 --preserve 
python manage.py makemigrations djangorest
python manage.py migrate djangorest
python manage.py runserver 0.0.0.0:8000
