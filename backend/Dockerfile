FROM python:3.12-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# -------------------- PRODUCTION STAGE --------------------
FROM python:3.12-slim

WORKDIR /app

RUN useradd -m -r appuser && \
   chown -R appuser /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY --chown=appuser:appuser . /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
USER appuser
 
EXPOSE 8000

CMD ["python", "run.py"]