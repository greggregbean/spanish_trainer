# Spanish Trainer

Spanish Trainer — это веб-приложение на Django для изучения испанского языка с использованием карточек и квиза.

Приложение позволяет:

* просматривать темы для изучения слов
* изучать карточки (испанское слово — перевод)
* добавлять новые карточки через форму
* проходить квиз с проверкой перевода

## Установка

### 1. Клонировать репозиторий
```bash
git clone https://github.com/greggregbean/spanish_trainer.git
```
### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install django
```

### 4. Применить миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создать администратора:

```bash
python manage.py createsuperuser
```

---

## Запуск

```bash
python manage.py runserver
```

Открыть в браузере:

```
http://127.0.0.1:8000/
```

Админ:

```
http://127.0.0.1:8000/admin/
```

## Автор
Зинин Иван, МФТИ ФРКТ М01-508
