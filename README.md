## Каталог исполнителей и их альбомов с песнями

API-сервис позволяет создавать и управлять каталогом исполнителей и их альбомами с песнями.

### Стек технологий

![Django-app workflow](https://github.com/needred/singers-drf-project/actions/workflows/app-testing.yml/badge.svg)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)

- проект написан на Python 3.10 с использованием Django REST Framework
- базы данных - SQLite3
- система управления версиями - git

## Установка и запуск

1. Cклонировать репозиторий `git@github.com:iricshkin/singers-drf-project.git`

2. Создать и заполнить .env файл по аналогии с .env.example

3. Запустить контейнер с сервисами

```
sudo docker-compose up -d --build
```

После запуска проекта, подробную инструкцию можно будет посмотреть по адресу http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/swagger/

### Примеры обращения к API:

- /swagger/ - Документация
- /albums/ - Получить список всех альбомов / Создать новый альбом
- /albums/{id}/ - Получить альбом по id / Обновить по id / Удалить по id
- /singers/ - Получить список всех исполнителей / Создать нового исполнителя
- /singers/{id}/ - Получить исполнителя по id / Обновить по id / Удалить по id
- /songs/ - Получить список всех песен / Создать новую песню
- /songs/{id}/ - Получить песню по id / Обновить по id / Удалить по id

### Об авторе

Ирина Фок [iricshkin](https://github.com/iricshkin/)
