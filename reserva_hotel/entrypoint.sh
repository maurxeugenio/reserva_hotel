#!/bin/sh

echo "Apply Database Migrations"
python manage.py migrate

echo "Run Tests"
python manage.py test

exec "$@"