#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py createsuperuser --no-input --username admin --email admin@admin.com
python manage.py load_cultures
python manage.py load_producers
python manage.py test

exec "$@"
