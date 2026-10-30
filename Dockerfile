FROM python:3.11-alpine3.24

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y setuptools wheel

RUN addgroup -S appuser && adduser -S -G appuser appuser

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8003

CMD ["gunicorn", "--bind", "0.0.0.0:8003", "app:app"]
