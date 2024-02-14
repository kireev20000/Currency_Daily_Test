# Справочная на курсам валют 

---

Django-приложение, отображает курс валюты по отношению к рублю на заданную дату по запросу пользователя на эндпоинт.   

---
 
***
## Особенности проекта
- Раздел admin для редактирования данных в БД.
- Кастомная команда для сбора актуальных данных с сайта ЦБ.


## Стек
- Python 3.11
- Django 4.2.4
- Django REST framework 3.14.0
- SQLite
___


## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:kireev20000/Currency_Daily_Test.git
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции 
```
python manage.py migrate
```
Выполнить загрузку информации в базу данных с сайта ЦБ:
```
python manage.py get_daily_currency_rates
```
Запустить локальный сервер
```
python manage.py runserver 8000
```

## Примеры запросов
Получение данных Get-запросом на эндпоинт.
```
http://localhost:8000/rate/?charcode=AUD&date=2024-01-01
```
Пример ответа на запроса. 
```
{
    "charcode": "AUD",
    "date": "2024-01-01",
    "rate": 57.0627
}
```
Использование с crontab, и другими планировщиками.

```
<baseDIR> python manage.py get_daily_currency_rates
```
## Об авторе <a id=7></a>

Киреев Александр Олегович  
Python-разработчик (Backend)  
E-mail: kireev20000@yandex.ru
Telegram: @kireev20000
