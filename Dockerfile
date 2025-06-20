# /Dockerfile

FROM python:3.11-slim

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Копируем зависимости и исходники заранее
COPY pyproject.toml poetry.lock README.md /app/
COPY ./src /app/src

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

RUN ls -la /app/src/kdkpbot

# Команда запуска
ENTRYPOINT ["poetry", "run", "python", "-u", "src/kdkpbot/main.py"]
