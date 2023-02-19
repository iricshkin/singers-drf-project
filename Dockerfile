FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV POETRY_HOME /opt/poetry
ENV PATH $POETRY_HOME/bin:$PATH
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VERSION=1.3.1

COPY poetry.lock pyproject.toml app/
WORKDIR /app

RUN apt -y update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && poetry install

COPY . /app

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ] 

