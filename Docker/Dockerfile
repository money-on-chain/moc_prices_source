FROM python:3.12-slim AS base
FROM base AS build

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/moc_prices_source
COPY . .
RUN python -m venv ../venv
RUN PIP_USE_DEPRECATED=legacy-certs \
    PIP_CERT=/etc/ssl/certs/ca-certificates.crt \
    ../venv/bin/pip install --upgrade 'pip>=26.2.2' setuptools wheel
RUN ../venv/bin/pip install -r requirements.lock.txt
RUN ../venv/bin/pip install .


# The runtime image ships the virtualenv only, without compilers or sources
FROM base

ENV PYTHONUNBUFFERED=1
ENV GUNICORN_WORKERS=2

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    redis \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Redis and the app run as this user (see supervisord.conf)
RUN useradd --create-home --uid 10001 app

COPY --from=build /app/venv /app/venv

RUN mkdir -p /etc/supervisor/conf.d
COPY Docker/files/supervisord.conf /etc/supervisor/supervisord.conf
COPY --chown=app:app Docker/files/conf/redis.json /home/app/.moc_prices_source/
COPY Docker/files/run.sh /
COPY Docker/files/check.sh /

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
