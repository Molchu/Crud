# Usa una imagen base de Python
FROM python:3.8-slim

# Establece la variable de entorno para evitar mensajes de advertencia de Python
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia todos los archivos del proyecto al directorio de trabajo del contenedor
COPY . .

# Expón el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host", "0.0.0.0"]