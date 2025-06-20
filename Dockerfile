FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && pip install --upgrade pip

# Устанавливаем Poetry надёжно
ENV POETRY_HOME="/opt/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
ADD https://install.python-poetry.org /tmp/install-poetry.py
RUN python3 /tmp/install-poetry.py && rm /tmp/install-poetry.py

# Настройка Poetry
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1

WORKDIR /app

# Копируем зависимости и README
COPY pyproject.toml poetry.lock README.md ./

# Установка зависимостей
RUN poetry install --no-ansi --no-root

# Копируем исходники
COPY src/ ./src
COPY tests/ ./tests

CMD ["python", "src/kdkpbot/main.py"]
