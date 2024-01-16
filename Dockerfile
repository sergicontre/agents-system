FROM python:3.9.16

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./app /app/
WORKDIR /app

# Ejecuta script.py cuando se lance el contenedor
CMD ["python", "engine.py"]