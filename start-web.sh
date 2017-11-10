#!/bin/bash
PGPASSWORD=$DATABASE_PASSWORD psql -U $DATABASE_USER -w -h $DATABASE_HOST -c "CREATE DATABASE ${DATABASE_NAME} OWNER ${DATABASE_USER}"
python3 manage.py migrate
python3 create_admin.py

crontab /etc/cron.d/audiencias
crond

exec daphne -b 0.0.0.0 -p 8000 audiencias_publicas.asgi:channel_layer