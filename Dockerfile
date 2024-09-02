# syntax=docker/dockerfile:1
FROM python:3.9-slim

WORKDIR /app

# Establecer variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Instalar las dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev-compat \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar y instalar las dependencias de Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo .env
COPY .env .env

# Exponer el puerto de la aplicación Flask
EXPOSE 8080

# Copiar el resto del código de la aplicación
COPY . .

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--port=8080"]

