#!/bin/sh

if [ "$DATABASE" = "mongo" ]
then
    echo "Waiting for mongo..."

    while ! nc -z $MONGO_HOST $MONGO_PORT; do
      sleep 0.1
    done

    echo "mongoDB started"
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
exec "$@"