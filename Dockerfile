# syntax=docker/dockerfile:1

FROM python:3.11-slim

# Обновим pip и установим curl
RUN apt-get update && apt-get install -y curl && pip install --upgrade pip

# Установим Poetry в /opt/poetry и добавим в PATH
ENV POETRY_HOME="/opt/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
ADD https://install.python-poetry.org install-poetry.py
RUN python3 install-poetry.py

# Отключаем виртуальные окружения и интерактивный режим
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы конфигурации poetry
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости
RUN poetry install --no-ansi

# Копируем исходники проекта
COPY src/ ./src
COPY tests/ ./tests

# Стандартная команда по умолчанию
CMD ["pytest"]
