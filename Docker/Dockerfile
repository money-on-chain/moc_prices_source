FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/moc_prices_source

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m venv .venv

RUN .venv/bin/pip install --upgrade pip setuptools wheel

RUN .venv/bin/pip install -r requirements.txt

RUN .venv/bin/pip install .

ENV API_HOST=0.0.0.0
ENV API_PORT=7990

CMD ["/bin/sh", "-c", ".venv/bin/moc_prices_source_api --addr \"$API_HOST\" --port \"$API_PORT\""]
