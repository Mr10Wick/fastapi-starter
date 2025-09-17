FROM python:3.10-slim

# curl pour le healthcheck
RUN apt-get -y update && apt-get -y install curl && rm -rf /var/lib/apt/lists/*

# répertoires et options python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# deps en premier pour profiter du cache
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# copier tout le code
COPY . .

# port FastAPI
EXPOSE 8000

# healthcheck simple : la doc swagger doit répondre
HEALTHCHECK --interval=1m --timeout=3s \
  CMD curl -sf http://localhost:8000/docs > /dev/null || exit 1

# entrypoint
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
