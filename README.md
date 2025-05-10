# Skypro-spa-app

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2-brightgreen.svg)
![DRF](https://img.shields.io/badge/drf-3.14-red.svg)
![Stripe](https://img.shields.io/badge/stripe-integration-635bff.svg)
![Celery](https://img.shields.io/badge/celery-5.3-green)


Backend API для платформы онлайн-обучения с интеграцией платежей через Stripe.

## 📌 Основные возможности

- **🔐 Аутентификация** через JWT-токены
- **📚 Управление курсами** и уроками
- **💰 Платежная система** через Stripe
- **🔔 Подписки** на курсы
- **📊 Админ-панель** для управления контентом
- **📧 Асинхронная рассылка уведомлений**
- **🔒 Автоматическая блокировка неактивных пользователей**
- **⏰ Периодические задачи с Celery Beat**

## 🚀 Быстрый старт

### Требования
- Python 3.9+
- PostgreSQL
- Stripe аккаунт
- Celery + Redis

### Установка

1. Клонируйте репозиторий:
```bash
  https://github.com/LeojBang/skypro-spa-app.git
```
2. Создайте и активируйте виртуальное окружение:
```bash
  python -m venv venv
```
```bash
  source venv/bin/activate  # Linux/MacOS
```
```bash
  venv\Scripts\activate    # Windows
```

3. Установите зависимости:
```bash
  pip install -r requirements.txt
```

4. Настройте окружение (создайте файл .env):
```
SECRET_KEY=ваш-secret-key
DEBUG=True

DB_NAME=learning_db
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
DB_PORT=5432

STRIPE_API_KEY=ваш-stripe-secret-key

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=ваш-email@yandex.ru
EMAIL_HOST_PASSWORD=ваш-пароль
EMAIL_USE_SSL=True

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

CACHE_ENABLED=True
REDIS_URL=redis://127.0.0.1:6379
```
5. Примените миграции:
```bash
    python manage.py migrate
```
6. Создайте суперпользователя:

```bash
  python manage.py csu
```

7. Запустите сервер:
#### Сервер будет доступен по адресу: http://localhost:8000/

```bash
  python manage.py runserver
```
8. Запуск Celery
```bash
# Worker
  celery -A config worker --loglevel=info
```
```bash
# Beat
celery -A config beat --loglevel=info
```
## 🌐 API Endpoints
### Аутентификация (users/)
```
Метод|	Эндпоинт	       | Описание
POST |	/users/register/       | Регистрация нового пользователя
POST |	/users/login/	       | Получение JWT токена
POST |	/users/token/refresh/  | Обновление JWT токена
```
### Курсы и уроки (lms/)
```
Метод  |	Эндпоинт	                   | Описание
GET    |	/lms/	                       | Список всех курсов (CRUD через ViewSet)
GET    |	/lms/lessons/	               | Список всех уроков
GET    |	/lms/lessons/<int:pk>/         | Получение конкретного урока
POST   |	/lms/lessons/create/           | Создание нового урока
PUT    |	/lms/lessons/<int:pk>/update/  | Обновление урока
DELETE |	/lms/lessons/<int:pk>/delete/  | Удаление урока
POST   |	/lms/subscriptions/            | Управление подписками на курсы
```
### Платежи (через Stripe)
```
Метод  |	    Эндпоинт	        | Описание
POST   |  /pay/course/<int:course_id>/  | Создание платежной сессии для курса
```



