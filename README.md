# Wizouri
Wizouri - сайт с интерактивной информацией о погоде в любой Стране/Городе в мире.
## Установка и запуск

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/TimurKurilov/Wizouri.git
cd Wizouri
```

### Шаг 2: Создание и активация виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. 

#### Использование venv (Python 3.3+)

```bash
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
```

### Шаг 3: Установка зависимостей

Убедитесь, что у вас установлен `pip`, затем установите зависимости из `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Шаг 4: Настройка Docker

Проект настроен для работы с Docker. Убедитесь, что у вас установлен Docker Desktop

#### Запуск проекта с помощью Docker Compose

```bash
docker-compose up --build
```

### Шаг 5: Миграции базы данных

После того как контейнеры запущены, выполните миграции базы данных:

```bash
docker-compose exec web python manage.py migrate
```

### Шаг 6: Создание суперпользователя

Создайте суперпользователя для доступа к административной панели Django:

```bash
docker-compose exec web python manage.py createsuperuser
```
### Шаг 7: создать статические файлы

```bash
docker-compose exec web python manage.py collectstatic --no-input
```

### Шаг 8: Доступ к приложению

Откройте ваш браузер и перейдите по адресу [http://localhost:8000](http://localhost:8000) для доступа к приложению.

## Дополнительная информация

- Для остановки контейнеров используйте команду `docker-compose down`.
- Для сборки контейнеров без кэша используйте команду `docker-compose build --no-cache`.
```
