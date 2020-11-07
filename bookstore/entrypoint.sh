#!/bin/sh

if [ "$DATABASE" = "mongo" ]
then
    echo "Waiting for mongo..."

    while ! nc -z $MONGO_HOST $MONGO_PORT; do
      sleep 0.1
    done

    echo "mongoDB started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py shell < import_mock_data.py
exec "$@"