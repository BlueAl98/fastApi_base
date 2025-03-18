FROM python:3.11

# Actualiza los repositorios e instala netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
COPY .env .
COPY app/ /app/

# Copia el script entrypoint.sh y le asigna permisos de ejecución
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la app
EXPOSE 8000

# Usa el script entrypoint.sh para esperar a que la base de datos esté disponible y arrancar la aplicación
ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
