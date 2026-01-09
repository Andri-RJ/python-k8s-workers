FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

ENV VERSION=1.0.0

RUN useradd -m -u 1000 worker && chown -R worker:worker /app
USER worker

EXPOSE 5000

CMD ["python", "app/main.py"]
