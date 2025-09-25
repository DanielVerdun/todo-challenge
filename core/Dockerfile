# Dockerfile para Django (producción)

# Usa una imagen base optimizada
FROM python:3.10-slim

# metadata
LABEL maintainer="tu-email@example.com"
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dependencias de runtime
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Crear usuario no-root y establecer permisos
ARG USER=app
ARG UID=1000
RUN groupadd -g ${UID} ${USER} \
    && useradd -m -u ${UID} -g ${UID} -s /bin/bash ${USER}

# **CORRECCIÓN CLAVE:** Copiar el código como el usuario root y luego cambiar el propietario
# Copiar e instalar dependencias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app/

# **CORRECCIÓN CLAVE:** Cambiar el propietario de todos los archivos de la aplicación al usuario `app`
RUN chown -R ${USER}:${USER} /app

# Exponer puerto y entrypoint
EXPOSE 8000
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Cambiar a usuario no-root
USER ${USER}

ENTRYPOINT ["/app/entrypoint.sh"]