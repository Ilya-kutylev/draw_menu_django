# Project draw-mune-django

<br>

## Contents:
- [Description](#description)
- [Technology](#technology)
- [Installation and startup](#installation-and-startup)

<br>

## Description

Tree menu is a Django application implemented with template tag. Menu by name can be drawn on any page of the
application using the following tags:

    {% load user_tags %}
    {% draw_menu menu_name menu_item %}

## Technology:

<details><summary>List</summary>

**Programming languages, libraries and modules:**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)

**Framework, extensions and libraries:**

[![Django](https://img.shields.io/badge/Django-v5.1-blue?logo=Django)](https://www.djangoproject.com/)

**Databases**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

[⬆️Contents](#contents)

</details>

## Installation and startup

Для Windows:

```bash
git clone git@github.com:ilya-kutylev/draw_menu_django.git
cd draw_menu_django
pipenv shell
pipenv install
python manage.py migrate
```

For the application to work correctly, you must:

- Create a superuser


```bash
python manage.py createsuperuser
```

- Add data through the administration panel
- Start the server

```bash
python manage.py runserver
```

