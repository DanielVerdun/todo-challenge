#!/bin/bash
set -e

echo "Iniciando la aplicación Django..."

# Exportar el settings correcto
export DJANGO_SETTINGS_MODULE=core.settings

# Ejecutar migraciones de Django y collectstatic
python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput

# Iniciar Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --workers 3 core.wsgi:application