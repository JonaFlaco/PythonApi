# Usa una versión actualizada de Python
FROM python:3.11-slim

# Actualiza la lista de paquetes disponibles e instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en /src
WORKDIR /src

# Copia solo el archivo requirements.txt y el código de la aplicación
COPY requirements.txt ./
COPY . .

# Actualiza pip y setuptools
RUN pip install --upgrade pip setuptools

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8000"]
