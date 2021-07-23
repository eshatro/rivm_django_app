FROM python:3.8-slim-buster

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /opt/virtualenv \
  && . /opt/virtualenv/bin/activate \
  && pip install -r /tmp/requirements.txt

ENV PYTHONUNBUFFERED=on
ENV PATH="/opt/virtualenv/bin:$PATH"

COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - rivm.wsgi:application
