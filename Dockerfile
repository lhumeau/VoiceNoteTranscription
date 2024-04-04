# Usar una imagen base oficial de Python
FROM python:3.8-slim

# Instalar openssl y ffmpeg
RUN apt-get update \
    && apt-get install -y openssl ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY main.py .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Generar un certificado SSL autofirmado
RUN openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com"

# Exponer el puerto que utilizará Uvicorn
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile=key.pem", "--ssl-certfile=cert.pem"]

