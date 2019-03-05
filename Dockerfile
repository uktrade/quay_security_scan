FROM python:3

WORKDIR /root/quaysecurityscan/
ADD . /root/quaysecurityscan/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT