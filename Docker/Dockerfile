FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-venv \
    redis \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/moc_prices_source
COPY . .
RUN python -m venv ../venv
RUN ../venv/bin/pip install --upgrade pip setuptools wheel
RUN ../venv/bin/pip install -r requirements.lock.txt
RUN ../venv/bin/pip install .
WORKDIR /app
RUN rm -rf ./moc_prices_source
WORKDIR /

RUN mkdir -p /etc/supervisor/conf.d
RUN mkdir /root/.moc_prices_source
COPY Docker/files/supervisord.conf /etc/supervisor/supervisord.conf
COPY Docker/files/conf/redis.json /root/.moc_prices_source/
COPY Docker/files/run.sh /
COPY Docker/files/check.sh /

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
