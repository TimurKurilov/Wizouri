FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY /server /app/server

CMD ["gunicorn", "--chdir", "server", "--bind", ":8000", "server.wsgi:application"]
