#!/bin/sh
set -e

echo "Esperando a que MariaDB esté disponible en db:3306..."
while ! nc -z db 3306; do
  sleep 1
done

echo "MariaDB está disponible. Arrancando FastAPI..."
exec "$@"