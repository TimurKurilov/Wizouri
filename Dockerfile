FROM python:3.11-slim

RUN mkdir /app

COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY server/ /app

WORKDIR /app

CMD ["gunicorn", "server.wsgi:application", "--bind", "0:8000" ]
